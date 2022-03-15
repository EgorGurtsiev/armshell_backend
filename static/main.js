function search_player() {
    let search = document.querySelector('#search');
    let s_nickname = search.value;
    if (s_nickname.length >= 3){
        let xhr = new XMLHttpRequest();
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

}

function debounce(callee, timeoutMs) {
    return function perform(...args) {
        let previousCall = this.lastCall;
        this.lastCall = Date.now();
        if (previousCall && this.lastCall - previousCall <= timeoutMs) {
            clearTimeout(this.lastCallTimer);
        }
        this.lastCallTimer = setTimeout(() => callee(...args), timeoutMs);
    };
}


let search_player_deb = debounce(search_player, 200)