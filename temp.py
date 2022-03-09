text='remind me'
if 'remind me' in text:
    import webbrowser
    text=text.replace('remind me after','')
    text=text.replace('minutes','')
    text=text.replace('seconds','')
    new_TEXT=text.split('and')
    if len(new_TEXT) == 1:
        secs='0'
    else:
        secs=str(new_TEXT[1])
        pass
    mins=str(new_TEXT[0])
    url='https://www.google.com/search?q=timer+'+mins+'+min+'+secs+'+sec&oq=timer+2+min+20+sec&aqs=chrome..69i57.4505j0j1&sourceid=chrome&ie=UTF-8'
    webbrowser.open(url)
 #   return( 'ok sir , I will remind you after',mins,'minutes','and',secs,'seconds')