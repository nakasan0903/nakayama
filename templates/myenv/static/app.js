document.getElementById('teamForm').addEventListener('submit', function(event) {
    event.preventDefault();
    const teamName = document.getElementById('teamName').value.toLowerCase();

    switch(teamName) {
        case 'manchester city':
            window.location.href = '/manchester-city.html';
            break;
        case 'manchester united':
            window.location.href = '/manchester-united.html';
            break;
        case 'liverpool':
            window.location.href = '/liverpool.html';
            break;
        case 'chelsea':
            window.location.href = '/chelsea.html';
            break;
        case 'arsenal':
            window.location.href = '/arsenal.html';
            break;
        case 'tottenham hotspur':
            window.location.href = '/tottenham-hotspur.html';
            break;
        default:
            alert('指定されたチームは見つかりませんでした。');
            break;
    }
});

