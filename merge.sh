
declare repo=$1

git remote add $repo git@github.com:matheustecchio/$repo.git
pause
git fetch $repo
git merge $repo/main --allow-unrelated-histories
mkdir $repo
git ls-tree -z --name-only $repo/main | xargs -0 -I {} git mv {} $repo/
git commit -m "Move $repo into subfolder"