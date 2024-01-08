document.getElementById('teamForm').addEventListener('submit', function(event) {
    event.preventDefault();
    let playerName = document.getElementById('teamName').value.toLowerCase();

    playerName = playerName.normalize("NFD").replace(/[\u0300-\u036f]/g, "").replace(/・/g, "").replace(/\s+/g, '');

    switch(playerName) {
        case 'アーロンラムズデール':
            window.location.href = '/ramsdale';
            break;
        // 他の選手のケースをここに追加
        default:
            alert('指定された選手は見つかりませんでした。');
            break;
    }
});
