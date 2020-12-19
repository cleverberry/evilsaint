import os

OUTPUT_PATH = 'C:\\Users\\Lemmeister\\Documents\\Visual Studio Code Workspace\\evilsaint\\_posts\\output.md'

f = open(os.path.join('C:\\Users\\Lemmeister\\Documents\\Visual Studio Code Workspace\\evilsaint\\_posts\\2020-12-19-infrastructure-pentesting-from-linux-box.md'))
index = 0
for line in f.readlines():
    if line == '```\n':
        if index % 2 == 0:
            line = '{% highlight PowerShell %}\n'
        else:
            line = '{% endhighlight %}\n'
        index = index + 1
    with open(OUTPUT_PATH, 'a') as filehandle:
        filehandle.write(line)
        filehandle.close()
f.close()