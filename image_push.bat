git checkout gh-pages
git pull 
git add docs/_posts/* docs/assets/* 1>>problems.txt 2>>problems2.txt
git commit -m "Added new post" 1>>problems.txt 2>>problems2.txt
git push 1>>problems.txt 2>>problems2.txt
