var fetch = require('node-fetch');


bitmasApi = {
  const url = 'https://bitmax.io/api/assets'


};






//get url and return json type data
fetch(url, {})
  .then((response) => {
    // 這裡會得到一個 ReadableStream 的物件
    // console.log('response= ', response);
    // console.log('typeof(response)= ', typeof(response))
    // console.log('response.status= ',response.status)
    // 可以透過 blob(), json(), text() 轉成可用的資訊
    return response.json();
  }).then((jsonData) => {
    data = jsonData;
    console.log('data.length= ', data.length)
    console.log('jsonData[0].assetId= ', jsonData[0].assetId);
  }).catch((err) => {
    console.log('錯誤:', err);
});
