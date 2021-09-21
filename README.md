# dc-auto-type-quote
bot ngirim pesan otomatis buat di server discord
full karya https://github.com/vsec7 ( https://github.com/vsec7/DC-Bot-Auto-Post )

buat dapetin token nya inject js nya di sini discord.com/app ( keadaan udah login di browser )

javascript:var i = document.createElement('iframe');i.onload = function(){var localStorage = i.contentWindow.localStorage;prompt('DC Token By @github.com/vsec7', localStorage.getItem('token').replace(/["]+/g, ''));};document.body.appendChild(i); 

F12 > Application > Storage > LocalStorage > https://discord.com > Ketik di pencarian dengan keyword "token"
