## Step by step guide to setting up a new serverless project

### Create a new serverless project

Most common way is to use templates, like so, which creates a new project scaffold in the current directory where the command is run:

```
serverless create --template aws-nodejs
```

The above template is quite bare bones, so a better starting point might be to use this starter project:

```
serverless install --url https://github.com/AnomalyInnovations/serverless-nodejs-starter --name my-project
```

Once you have this downloaded you will need to install dependencies:

```
npm i
npm install aws-sdk --save-dev
```

Sanity check:

```
sls invoke local -f hello
```

Now, setup the project structure so that the lambda functions, library functions, mocks, aws resources, starter readme are in their own folder

1. `mkdir endpoints libs resources mocks starter`
1. `mv handler.js endpoints`
1. `mv README.md starter`
1. `mv env.example .env`
1. `touch README.md`

Now update the `serverless.yml` for the new location of the `handler.js`

```
functions:
  hello:
    handler: endpoints/handler.hello
    ...
```

...also update the import statement at the top of the test file like so:

```
import * as handler from '../endpoints/handler';
...
```

Now test the function again which should work as usual:

```
sls invoke local -f hello
```

Now check the unit tests are running;

```
npm run test
```

### Setup AWS IAM Account keys ready for deployment

Serverless CLI uses the AWS CLI, so you will need to [install the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html) first.

Now configure AWS CLI. If you are working on several projects then you can optionally pass the `--profile` flag as [explained here](https://serverless-stack.com/chapters/configure-multiple-aws-profiles.html).

```
aws configure --profile myproject
```

Set the profile for the duration of the session with an environment variable:

```
export AWS_PROFILE=myproject
```

You should also update your `serverless.yml` with the profile so its picked up correctly during deployment:

```
service: service-name

provider:
  name: aws
  stage: dev
  profile: myproject
```

Now deploy the application which will default to the `dev` stage:

```
sls deploy
```

### Add support to deploy to different stages

Update the `serverless.yml` file so that you can deploy using different stages. Add this following 'custom' section:

```
custom:
  # Below stage setting telling Serverless to first look for the opt:stage (the one passed in through the command line), and then fallback to self:provider.stage (the one in the provider block).
  stage: ${opt:stage, self:provider.stage}
```

So with the above the default will be the value set in the `provider.stage` section of the file, unless you pass in a specific stage via the `-s` switch like so:

```
sls deploy -s prod
```

### Info

To get information about a particular stage:

```
sls info -s dev -v
```

### Print the compiled config file

Useful to verify that the `serverless.yml` is setup ok:

```
sls print
```

## Add lib helper functions for debug, api responses and dynamodb

Add the following functions to your lib directory that will really help with the application development.

Create the file **lib/apiResponses-lib.js** and add the following code:

```
export default {
  _200(data = {}) {
      return {
          statusCode: 200,
          body: data,
      };
  },

  _400(data = {}) {
      return {
          statusCode: 400,
          body: data,
      };
  },

  _404(data = {}) {
    return {
        statusCode: 404,
        body: data,
    };
  },
};
```

Create the file **lib/debug-lib.js** and add the following code:

```
import util from "util";
import AWS from "aws-sdk";

let logs;

// Log AWS SDK calls
AWS.config.logger = { log: debug };

export default function debug() {
  logs.push({
    date: new Date(),
    string: util.format.apply(null, arguments),
  });
}

export function init(event, context) {
  logs = [];

  // Log API event
  debug("API event", {
    body: event.body,
    pathParameters: event.pathParameters,
    queryStringParameters: event.queryStringParameters,
  });
}

export function flush(e) {
  logs.forEach(({ date, string }) => console.debug(date, string));
  console.error(e);
}
```

Create the file **lib/dynamodb-lib.js** and add the following code:

```
import AWS from "aws-sdk";

const client = new AWS.DynamoDB.DocumentClient();

export default {
  get   : (params) => client.get(params).promise(),
  put   : (params) => client.put(params).promise(),
  query : (params) => client.query(params).promise(),
  scan  : (params) => client.scan(params).promise(),
  update: (params) => client.update(params).promise(),
  delete: (params) => client.delete(params).promise(),
};
```

Create the file **lib/handler-lib.js** and add the following code:

```
import * as debug from "./debug-lib";

export default function handler(lambda) {
  return async function (event, context) {
    let res, statusCode, body;

    // Start debugger
    debug.init(event, context);

    try {
      // Run the Lambda
      res = await lambda(event, context);
      statusCode = res.statusCode;
      body = res.body;
    } catch (e) {
      // Print debug messages
      debug.flush(e);

      body = { error: e.message };
      statusCode = 500;
    }

    // Return HTTP response
    return {
      statusCode,
      body: JSON.stringify(body),
      headers: {
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Credentials": true,
      },
    };
  };
}
```

Now you have some useful helper functions available for your serverless app to use.

## Update the function to say hello

As a check things are wired up correctly, lets change the function so that it will say hi to us - so a basic 'hello world' that will return our name.

First update the function like so. Note how we now make use of the library files we just copied over.

```
import handler from "../libs/handler-lib";
import Responses from '../libs/apiResponses-lib';

export const main = handler(async (event, context) => {
  let msg = { message: `Hello ${event.pathParameters.name}!` };
  return Responses._200(msg);
});
```

Now create the following file **mocks/hello.json** which we will use to invoke the function and pass in the 'name; param:

```
{
  "pathParameters": {
    "name": "Darren"
  }
}
```

Now test this function locally.

```
sls invoke local -f hello --path mocks/hello.json
```

If the function is working, go ahead and update the service in AWS with these changes (below is how you can deploy a single function rather than the entire stack):

```
sls deploy -f hello
```

## Define AWS Resources

Now we can use the power of serverless / cloudformation to define our resources so that they are created the same way everytime. This is scripting infrastructure setup.

### DynamoDB Resource

In `resources` folder, create a new file `dynamodb-table.yml` and define your tables in the file. For example, the configuration below will create two tables - one to hold 'referrals' and another to hold the 'referral count'.

The cloudformation documentation for [creating DynamoDb tables](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_DynamoDB.html).

```
Resources:
  ReferralsTable:
    Type: AWS::DynamoDB::Table
    Properties:
      TableName: ${self:custom.dynamodb.tableName}
      AttributeDefinitions:
        - AttributeName: referralId
          AttributeType: S
      KeySchema:
        - AttributeName: referralId
          KeyType: HASH
      # Set the capacity to auto-scale
      BillingMode: PAY_PER_REQUEST
  ReferralsCountTable:
    Type: AWS::DynamoDB::Table
    Properties:
      TableName: ${self:custom.dynamodb.tableNameCount}
      AttributeDefinitions:
        - AttributeName: userId
          AttributeType: S
      KeySchema:
        - AttributeName: userId
          KeyType: HASH
      # Set the capacity to auto-scale
      BillingMode: PAY_PER_REQUEST
```

### S3 Bucket resources

In `resources` folder, create a new file `s3-bucket.yml` and define your tables in the file. S3 buckets can be created as follows:

```
Resources:
  AttachmentsBucket:
    Type: AWS::S3::Bucket
    Properties:
      BucketName: ${self:custom.s3.bucketAttachments}
      # Set the CORS policy
      CorsConfiguration:
        CorsRules:
          -
            AllowedOrigins:
              - '*'
            AllowedHeaders:
              - '*'
            AllowedMethods:
              - GET
              - PUT
              - POST
              - DELETE
              - HEAD
            MaxAge: 3000

# Print out the name of the bucket that is created
Outputs:
  AttachmentsBucketName:
    Value:
      Ref: AttachmentsBucket
```

### Update the serverless file with the new resources

Once you have created all the resources you want then you also need to add them to the serverless.yml file:

```
# Create our resources with separate CloudFormation templates
resources:
  # DynamoDB
  - ${file(resources/dynamodb-table.yml)}
  # S3
  - ${file(resources/s3-bucket.yml)}
```

### Add IAM service policies

THe `iamRoleStatements` section of the `serverless` file  defines the permission policy for the Lambda function. These will be created under IAM -> Roles in the AWS Console and will be named related to the service, stage and role e.g. 'referral-api-dev-lambda'.

Add the following IAM policy which will allow:

* All actions to be performed on dynamodb
* S3 objects to be fetched via GetObject
* Lambda functions to be invoked.

More over the reources allowed are:

* The `ReferralsTable` as defined in the DynamoDb resource
* The `ReferralsCountTable` as defined in the DynamoDb resource
* The `AttachmentsBucket` as defined in the S3 resource

```
iamRoleStatements:
    - Effect: Allow
      Action:
        - dynamodb:*
        - s3:GetObject
        - lambda:InvokeFunction
        - lambda:InvokeAsync
      Resource:
        - "Fn::GetAtt": [ ReferralsTable, Arn ]
        - "Fn::GetAtt": [ ReferralsCountTable, Arn ]
        - Fn::Join: ['', [Fn::GetAtt: [ AttachmentsBucket, Arn ], '/*'] ]
```

### Calling an IAM Authorized API Gateway endpoint

There are several ways of doing this depending on your usecase:

* Testing you can use [Postman](https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-use-postman-to-call-api.html) or the [AWS Console](https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-test-method.html)
* In a client that uses Cognito like a mobile or web app, then use [AWS Amplify](https://docs.amplify.aws/lib/restapi/getting-started/q/platform/js) which integrates nicely with Cognito to provide session based authentication.
* In a standalone client, for exmple a service use the [sigV4Client.js](https://raw.githubusercontent.com/AnomalyInnovations/sigV4Client/master/sigV4Client.js) with the [crypto-js](https://www.npmjs.com/package/crypto-js) library. This is the best approach (for a standalone client) since it just requires one file to be copied over and one libary to be installed.

### Example of using in a standalone client

Here are the details of how you might go about that:

Copy the [sigV4Client.js](https://raw.githubusercontent.com/AnomalyInnovations/sigV4Client/master/sigV4Client.js) file into your project.

Install the crypto-js libraray: `npm install crypto-js --save`

Copy the following helper function into your project:

```
const { sigV4Client } = require('sigV4Client') // assuming you have copied sigV4Client in the same directory

async function invokeApig({
  path,
  method = "GET",
  headers = {},
  queryParams = {},
  body
}) {
  const signedRequest = sigV4Client
    .newClient({
      accessKey: YOUR_ACCESS_KEY_ID,
      secretKey: YOUR_SECRET_KEY_ID,
      // sessionToken: '', // only required when using temp credentials
      region: YOUR_AWS_REGION
      endpoint: YOUR_APIG_ENDPOINT
    })
    .signRequest({
      method,
      path,
      headers,
      queryParams,
      body
    });

  body = body ? JSON.stringify(body) : body;
  headers = signedRequest.headers;

  console.log('*** signedRequest.headers', signedRequest.headers)
  console.log('*** signedRequest.url', signedRequest.url)

  const results = await fetch(signedRequest.url, {
    method,
    headers,
    body
  });

  if (results.status !== 200) {
    throw new Error(await results.text());
  }

  return results.json();
}

exports.invokeApig = invokeApig
```

You can use this helper in your main app as follows:

```
let response = await invokeApig({path: '/yourpath'})
```
