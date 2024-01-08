document.addEventListener('DOMContentLoaded', function() {
    const API_KEY = 'Daniel Freitag - Daniel@football-data.org - Version 2.0 | June 31 | 2018'; // ここに実際のAPIキーを設定してください
    const API_URL = 'http://api.football-data.org/v2/competitions/'; // APIのエンドポイント

    fetch(API_URL, {
        method: 'GET',
        headers: {
            'X-Auth-Token': API_KEY
        }
    })
    .then(response => {
        if (!response.ok) {
            throw new Error("Network response was not ok");
        }
        return response.json();
    })
    .then(data => {
        console.log(data); // コンソールでデータを確認
        document.getElementById('data').innerHTML = JSON.stringify(data, null, 2);
        // 必要に応じてデータを加工して表示
    })
    .catch(error => {
        console.error('Fetch error:', error);
        document.getElementById('data').innerHTML = 'Data could not be loaded';
    });
});
