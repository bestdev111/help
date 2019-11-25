# Bash Profile

```
export EDITOR=nano
export KOPS_STATE_STORE=s3://kops-state-rt7665

export NVM_DIR="/Users/darren/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm
# added by Anaconda3 5.2.0 installer
export PATH="/anaconda3/bin:$PATH"

eval "$(rbenv init -)"

# for activating a python environment
alias venv="source venv/bin/activate"
alias fl="networksetup -setairportpower en0 off; sudo route flush; networksetup -setairportpower en0 on;"
alias rs="bundle exec rails s"
alias rc="bundle exec rails c"
alias gs='git status '
alias ga='git add '
alias gb='git branch '
alias gc='git commit'
alias gd='git diff'
alias go='git checkout '
alias eh='cd ~/workspace/help; code .'
alias ks='kubectl'
alias dc='docker-compose'
alias dp='docker ps'
alias di='docker images'
alias wk='cd ~/workspace/'
alias wkp='cd ~/workspace/rotati/pyful/py-api'
alias wkv='cd ~/workspace/rotati/pyful/vue-crypto'
alias wko='cd ~/workspace/rotati/oscar-web'
alias wkt='cd ~/workspace/tigerbee/tb-bot-ruby'
alias wkl='cd ~/workspace/learning/ML/machine-learning-with-python'
alias wkh='cd ~/workspace/help/'
dexec() { docker exec -it "$1" bash; }
drun() { docker run -it --entrypoint bash -v "$PWD":"$1" "$2"; }
dclean() { docker stop $(docker ps -a -q); docker rm -f $(docker ps -a -q); docker rmi -f $(docker images | grep "<none>" | awk "{print \$3}"); docker system prune -f; docker system prune --volumes -f; }
ch() { cd ~/workspace/help/; git add .; git commit -m 'Update help'; git push origin master; }
```