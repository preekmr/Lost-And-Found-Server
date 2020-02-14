cd ./ui
npm install
npm run build
rm -rf ../templates/*
rm -rf ../static/*
cp dist/* ../static/
cp dist/index.html ../templates/