import yt_dlp

   ydl_opts = {
       'cookiefile': 'cookies.txt',
       # other options...
   }

   with yt_dlp.YoutubeDL(ydl_opts) as ydl:
       ydl.download(['https://youtube.com'])
   
