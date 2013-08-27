#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import markdown
import codecs
from Cheetah.Template import Template

themes = {
    'themeblack': [os.sep.join([os.path.dirname(__file__), 'themecss', 'black', css]) for css in ['preview.css', 'style.css']],
    'themewhite': [os.sep.join([os.path.dirname(__file__), 'themecss', 'white', css]) for css in ['markdown.css']]
}


templateDef_themeblack = '''
#encoding utf-8
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en-US" lang="en-US">
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>$title</title>
        #for $cssfile in $css
            <link href="file:///$cssfile" rel="stylesheet" type="text/css">
        #end for
    </head>
        <body>
            <div id="preview_pane" class="pane" style="width: 780px;">
                <div id="preview">$content</div>
            </div>
        </body>
</html>
'''

templateDef_themewhite = '''
#encoding utf-8
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en-US" lang="en-US">
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>$title</title>
        #for $cssfile in $css
            <link href="file:///$cssfile" rel="stylesheet" type="text/css">
        #end for
    </head>
        <body>
            $content
        </body>
</html>
'''


def md2html(mdfile, htmlfile, theme):
    '''
        mdfile: 需要转换的markdown的完整路径
        htmlfile: 需要生成html文件的完整路径
        theme: themes中任选其中一个
    '''
    # Open input file in read, utf-8 mode
    input_file = codecs.open(mdfile, mode="r", encoding="utf8")
    text = input_file.read()
    content = markdown.markdown(text)
    nameSpace = {
        'title': u'',
        'content': content,
        'css': themes[theme]
    }
    currentmodule = __import__('md2html')
    template = getattr(currentmodule, 'templateDef_%s' % theme)
    html = Template(template, searchList=[nameSpace])
    # Write string html to disk
    with open(htmlfile, 'wb') as f:
        f.write(str(html))


def main():
    mdfile = os.sep.join([os.getcwd(), 'demo.md'])
    htmlfile = os.sep.join([os.getcwd(), 'demo.html'])
    # md2html(mdfile, htmlfile, 'themewhite')
    md2html(mdfile, htmlfile, 'themeblack')

if __name__ == '__main__':
    main()
