function search_player() {
    let xhr = new XMLHttpRequest();
    let search = document.querySelector('#search');
    let s_nickname = search.value;

    s_nickname = encodeURIComponent(s_nickname);

    xhr.open('GET', '/players/search/?nickname=' + s_nickname);
    xhr.send()

    xhr.onreadystatechange = function() {
        if(xhr.readyState === 4 && xhr.status === 200) {
            let ls_players = document.querySelector('#ls_players');
            let lis = document.createElement('span');
            lis.id = "ls_players";
            for (let nickname of JSON.parse(xhr.responseText)) {
                let li = document.createElement('li');

                nickname = nickname.nickname;
                li.innerHTML = '<a class="dropdown-item" href="/players/' + nickname + '">' + nickname + '</a>';
                lis.append(li)
            }
            console.log(lis)
            ls_players.replaceWith(lis)
        }
    }
}




