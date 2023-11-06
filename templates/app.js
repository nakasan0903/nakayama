document.getElementById('teamForm').addEventListener('submit', function(event) {
   //document.getElementById('teamForm'):html内の属性がteamFormの要素を取得
   //addEventListener('submit',function(event){...}':'teamForm'というフォームの'submit'イベント
   //が発生した時に、指定した関数を実行するようにイベントリスナーを追加している。
   event.preventDefault(); 
   //通常、フォームが送信されると、ページは再読み込みされます。しかし、event.preventDefault()を使用すると、
   //そのデフォルトの動作をキャンセルし、ページの再読み込みなしにJavaScriptでカスタムの動作を行うことができます
    const teamName = document.getElementById('teamName').value;
    
    switch(teamName.toLowerCase()) {
        case 'arsenal':
        case 'Arsenal':
        case 'アーセナル':
        window.location.href = 'arsenal.html';
            break;
        case 'chelsea':
            window.location.href = 'chelsea.html';
            break;
        case 'liverpool':
            window.location.href = 'chelsea.html';
            break;
        case 'city':
            window.location.href = 'chelsea.html';
            break;
        case 'united':
            window.location.href = 'chelsea.html';
            break;
        case 'spurs':
            window.location.href = 'chelsea.html';
            break;
        default:
            alert('指定されたチームは見つかりませんでした');
            break;
    }
});
