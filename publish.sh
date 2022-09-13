source .env
git clone $REPOSITORY_URL
python manage.py build --keep-build-dir
cd portfolio-website
git add .

if git status --porcelain | grep "^A"; then
  echo 'Warning!! A new file has been added. Please commit and push manually'
else
  git commit -m "$1"
  git push
fi
cd ..
