## npm

List all local packages

```
npm list
```

List all global packages

```
npm list -g
```

List a specific global package (e.g. serverless)

```
npm list -g serverless
```

Set the default version of node for the system (e.g. version 12.x)

```
nvm alias default 12
```

Use a specific version of node (e.g. version 12)

```
nvm use 12
```

View the global node_modules path

```
npm root -g
```

Linking a local module into a local project

For example, you want to load a locally cloned module into a local project so that you can easily test changes to that module

Taken from [this article](https://medium.com/@alexishevia/the-magic-behind-npm-link-d94dcb3a81af)

```
# Clone some random node module like randomstring!
cd ~/Desktop
git clone git@github.com:klughammer/node-randomstring.git

# Run npm link in that modules folder
cd ~/Desktop/node-randomstring
npm link

# In your local project run npm link linked-module-name e.g.
cd ~/Desktop/my-project
npm link randomstring

# Now require that module like normal:
# ~/Desktop/my-project/app.js
const randomstring = require("randomstring");
console.log(randomstring.generate());
```
