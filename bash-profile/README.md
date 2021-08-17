export EDITOR=nano
export KOPS_STATE_STORE=s3://kops-state-rt7665

 # This loads nvm
export NVM_DIR="/Users/darren/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"
# added by Anaconda3 5.2.0 installer
# export PATH="/anaconda3/bin:$PATH"
export PATH=$HOME/.gem/ruby/2.6.0/bin:$PATH
# elixir path
export PATH="$PATH/usr/local/bin/elixir"
# Radicle path
export PATH="$HOME/.radicle/bin:$PATH"

# This loads rbenv
eval "$(rbenv init -)"

# This loads pyenv
export PATH="/Users/darren/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"

# For activating a python environment
alias venv="source venv/bin/activate"
# Flush the network
alias fl="networksetup -setairportpower en0 off; sudo route flush; networksetup -setairportpower en0 on;"
# Rails alias
alias rs="bundle exec rails s"
alias rc="bundle exec rails c"
# Git alias
alias gs='git status '
alias ga='git add '
alias gb='git branch '
alias gc='git commit'
alias gd='git diff'
# Docker alias
alias ks='kubectl'
alias dc='docker-compose'
alias dp='docker ps'
alias di='docker images'
# Help
alias oh='open https://github.com/jensendarren/help'
# Working directory alias
alias wk='cd ~/workspace/'
alias wkcfi='cd ~/workspace/devzep/cfi-referral'
alias wks='cd ~/workspace/bot/sobot'
alias wkb='cd ~/workspace/upwork/karam/bot/unitrade-bot'
alias wkz='cd ~/workspace/upwork/karam/ze/zeplatform'
alias wko='cd ~/workspace/devzep/oscar/repo/oscar-web'
alias wkt='cd ~/workspace/archive/tigerbee'
alias wkh='cd ~/workspace/help/'
alias wku='cd ~/workspace/udacity/blockchain/'
alias wkpn='cd ~/workspace/pn/pointnetwork'
alias wkpy='cd ~/workspace/udacity/aifortrading/jupyter'

# Point Network
alias point-1="export DATABASE_URL='postgres://pointuser:pointpassword@localhost:5432/point_storage_provider' && npx knex migrate:latest && ./point --datadir ~/.point/test1 -v"
alias point-2="export DATABASE_URL='postgres://pointuser:pointpassword@localhost:5432/point_website_owner' && npx knex migrate:latest && npx nodemon ./point --datadir ~/.point/test2"
alias point-2-debug="./point --datadir ~/.point/test2"
alias point-3="export DATABASE_URL='postgres://pointuser:pointpassword@localhost:5432/point_website_visitor' && npx knex migrate:latest && ./point --datadir ~/.point/test3 -v"
alias point-nuke="./point debug-destroy-everything --datadir ~/.point/test1; ./point debug-destroy-everything --datadir ~/.point/test2; ./point debug-destroy-everything --datadir ~/.point/test3"
alias point-docker="docker-compose -f docker-compose.yaml -f docker-compose.dev.yaml up -d"
alias point-sdk="web-ext run --firefox-profile=website_owner --source-dir dist/prod --url https://hello.z/"

# Docker helper functions
dexec() { docker exec -it "$1" bash; }
dcr() { docker-compose run --rm "$@"; }
drun() { docker run -it --entrypoint bash -v "$PWD":"$1" "$2"; }
dclean() { docker stop $(docker ps -a -q); docker rm -f $(docker ps -a -q); docker rmi -f $(docker images | grep "<none>" | awk "{print \$3}"); docker system prune -f; docker system prune --volumes -f; }
# Local help file managment
alias eh='cd ~/workspace/help; code .'
ch() { cd ~/workspace/help/; git add .; git commit -m 'Update help'; git push origin master; }
source "$HOME/.cargo/env"

# transfer.sh

transfer(){ if [ $# -eq 0 ];then echo "No arguments specified.\nUsage:\n transfer <file|directory>\n ... | transfer <file_name>">&2;return 1;fi;if tty -s;then file="$1";file_name=$(basename "$file");if [ ! -e "$file" ];then echo "$file: No such file or directory">&2;return 1;fi;if [ -d "$file" ];then file_name="$file_name.zip" ,;(cd "$file"&&zip -r -q - .)|curl --progress-bar --upload-file "-" "https://transfer.sh/$file_name"|tee /dev/null,;else cat "$file"|curl --progress-bar --upload-file "-" "https://transfer.sh/$file_name"|tee /dev/null;fi;else file_name=$1;curl --progress-bar --upload-file "-" "https://transfer.sh/$file_name"|tee /dev/null;fi;}
