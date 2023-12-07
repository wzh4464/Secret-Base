

# Latexdiff with subfiles - TeX - LaTeX Stack Exchange --- 带有子文件的 Latexdiff - TeX - LaTeX 堆栈交换

# 

[↓↓↓](https://tex.stackexchange.com/questions/167620/latexdiff-with-subfiles)  
  
Latexdiff with subfiles 带有子文件的 Latexdiff  
  
[↑↑↑](https://tex.stackexchange.com/questions/167620/latexdiff-with-subfiles)

[↓↓↓](https://tex.stackexchange.com/questions/ask)  
  
Ask Question  
  
[↑↑↑](https://tex.stackexchange.com/questions/ask)

Asked 9 years, 8 months ago

Modified [2 years, 6 months ago](https://tex.stackexchange.com/questions/167620/latexdiff-with-subfiles?lastactivity "2021-05-26 20:18:39Z")

Viewed 20k times

21

[↓↓↓](https://tex.stackexchange.com/posts/167620/timeline)  
  
  
  
[↑↑↑](https://tex.stackexchange.com/posts/167620/timeline)

Is there a way to make latexdiff work with the 'subfiles' package ?  
有没有办法让 latexdiff 与“子文件”包一起使用？

I use subfiles to include parts of the document from different .tex files. Latexdiff does not seem to mark changes in the subfiles.  
我使用子文件来包含来自不同 .tex 文件的文档部分。Latexdiff 似乎没有标记子文件中的更改。

The --flatten option does not help. Latexdiff version is 1.0.2.  
\--flatten 选项无济于事。Latexdiff 版本为 1.0.2。

Example :  例：

main.tex

```latex
\documentclass[10pt]{article}
\usepackage{subfiles}
\begin{document}
\subfile{includeme.tex}
\end{document}  
```

includeme.tex 包括我.tex

```latex
\documentclass[main.tex]{subfiles} 
\begin{document}
Text!
\end{document}
```

Running  运行

```latex
latexdiff d1/main.tex d2/main.tex --flatten > mydiff.tex
```

the resulting document simply does not include the contents of the subfile.  
生成的文档根本不包含子文件的内容。

mydiff.tex

```latex
\documentclass[10pt]{article}
%DIF LATEXDIFF DIFFERENCE FILE
%DIF (...)
%DIF END PREAMBLE EXTENSION ADDED BY LATEXDIFF
\begin{document}
\subfile{includeme.tex}
\end{document}
```

So yes, the problem lies with the flatten pipeline/workflow, which does not seem to be made to work with \\subfile{includeme.tex} includes.  
所以是的，问题出在扁平化的管道/工作流上，它似乎不适用于 \\subfile{includeme.tex} 包含。

*   [latexdiff](https://tex.stackexchange.com/questions/tagged/latexdiff "show questions tagged 'latexdiff'")
*   [subfiles](https://tex.stackexchange.com/questions/tagged/subfiles "show questions tagged 'subfiles'")

[Share](https://tex.stackexchange.com/q/167620/157212 "Short permalink to this question")

[Edit](https://tex.stackexchange.com/posts/167620/edit "Revise and improve this post")

Follow

Flag

[edited Mar 26, 2014 at 14:23](https://tex.stackexchange.com/posts/167620/revisions "show all edits to this post")

asked Mar 25, 2014 at 16:21

[![mfit's user avatar](assets/1701949396-27a7c6d4120c22e9b934cd13ba1b712b.jpg)](https://tex.stackexchange.com/users/48627/mfit)

[mfit](https://tex.stackexchange.com/users/48627/mfit)

31311 gold badge22 silver badges66 bronze badges

*   [↓↓↓](# "This comment adds something useful to the post")  
      
      
      
    [↑↑↑](# "This comment adds something useful to the post")
    
    You could try some of the `flatten` alternatives discussed here: [tex.stackexchange.com/questions/21838/…](http://tex.stackexchange.com/questions/21838/replace-inputfilex-by-the-content-of-filex-automatically "replace inputfilex by the content of filex automatically")  
    您可以尝试此处讨论的一些 `flatten` 替代方案：tex.stackexchange.com/questions/21838/...
    
    – [Jörg](https://tex.stackexchange.com/users/11984/j%c3%b6rg "7,643 reputation")
    
    [Mar 26, 2014 at 10:51](#comment385791_167620)
    
*   [↓↓↓](# "This comment adds something useful to the post")  
      
      
      
    [↑↑↑](# "This comment adds something useful to the post")
    
    Could you add a MWE or at least a snippet of code that demonstrates how `subfiles` includes subsidiary files.  
    您能否添加一个 MWE 或至少一段代码来演示如何 `subfiles` 包含子文件。
    
    – [frederik](https://tex.stackexchange.com/users/38437/frederik "1,375 reputation")
    
    [Mar 26, 2014 at 11:14](#comment385801_167620)
    
*   [↓↓↓](# "This comment adds something useful to the post")  
      
      
      
    [↑↑↑](# "This comment adds something useful to the post")
    
    @f-tilman Added the MWE  
    @f-tilman 添加了 MWE
    
    – [mfit](https://tex.stackexchange.com/users/48627/mfit "313 reputation")
    
    [Mar 26, 2014 at 14:23](#comment385870_167620)
    
*   [↓↓↓](# "This comment adds something useful to the post")  
      
      
      
    [↑↑↑](# "This comment adds something useful to the post")
    
    Well, latexdiff does not know that it should expand the `\subfile` argument. You can adapt some of the scripts mentioned in the link before to use `\subfile` in a similar way as `\input`, but as your example of `includeme.tex` includes a `documentclass` I think it's not going to be compilable.  
    好吧，latexdiff 不知道它应该扩展 `\subfile` 参数。您可以调整之前链接中提到的一些脚本，以类似的方式使用 `\subfile` `\input` ，但是由于您的示例 `includeme.tex` 包括我认为 `documentclass` 它不会是可编译的。
    
    – [Jörg](https://tex.stackexchange.com/users/11984/j%c3%b6rg "7,643 reputation")
    
    [Mar 26, 2014 at 14:28](#comment385876_167620)
    
*   1
    
    [↓↓↓](# "This comment adds something useful to the post")  
      
      
      
    [↑↑↑](# "This comment adds something useful to the post")
    
    _For posterity:_ at least as of `latexdiff version 1.1.1`, using the `--flatten` option worked for me with subfiles. It took a little tweaking of the file-structure to get it to work, then I had to manually modify the resulting `mydiff.tex` slightly to get it to build into a PDF... but it worked.  
    对于后代：至少截至 `latexdiff version 1.1.1` ，使用该 `--flatten` 选项对我有用的子文件。它需要对文件结构进行一些调整才能使其工作，然后我不得不手动修改结果 `mydiff.tex` 以使其构建为 PDF......但它奏效了。
    
    – [DilithiumMatrix](https://tex.stackexchange.com/users/22806/dilithiummatrix "595 reputation")
    
    [Jun 1, 2017 at 12:58](#comment921132_167620)
    

[Show **1** more comment](# "Expand to show all comments on this post")

## 3 Answers

Sorted by:

Highest score (default) Date modified (newest first) Date created (oldest first)

8

[↓↓↓](https://tex.stackexchange.com/posts/167894/timeline)  
  
  
  
[↑↑↑](https://tex.stackexchange.com/posts/167894/timeline)

Note that the following is a work-around rather than a full solution:  
请注意，以下是一种解决方法，而不是完整的解决方案：

`latexdiff --append-safecmd=subfile d1/main.tex d2/main.tex --flatten > mydiff.tex`

will take care of the cases where a \\subfile command has been added or removed from the file, and the whole block is marked up (only tested on the MWE, would need to be confirmed for longer included material), or the filename of included file changes. You would still need to copy the included files into the directory where the difference file is generated (current directory in the MWE).  
将处理在文件中添加或删除 \\subfile 命令，并且整个块被标记（仅在 MBE 上测试，需要确认更长的包含材料）或包含文件更改的文件名的情况。您仍需要将包含的文件复制到生成差异文件的目录（MWE 中的当前目录）中。

To highlight content changes to the subfiles, you can process each file separately  
要突出显示对子文件的内容更改，可以单独处理每个文件

`cat /dev/null > null latexdiff -pnull d1/includeme.tex d2/includeme.tex > includeme.tex`

The -p option forces latexdiff to omit the preamble commands that it normally inserts automatically when it finds a \\begin{document} (auxiliary file "null" is needed as -p/dev/null is not recognised due to a bug in latexdiff).  
\-p 选项强制 latexdiff 省略它通常在找到 \\begin{document} 时自动插入的前导码命令（需要辅助文件“null”，因为由于 latexdiff 中的错误无法识别 -p/dev/null）。

Now all that remains is to automate this. The following line is a hacky way to achieve some automation as proof-of-concept but would really need to be expanded into a more robust and flexible small shell script:  
现在剩下的就是自动化。以下行是实现一些自动化作为概念验证的黑客方法，但实际上需要扩展为更强大、更灵活的小 shell 脚本：

`grep -v '^%' main.tex | grep subfile\{ | sed 's/^.*subfile{\(.*\)}.*$/\1/' \ | awk '{ print "latexdiff -pnull d1/" $1, "d2/" $1,">", $1 }' | sh`

[Share](https://tex.stackexchange.com/a/167894/157212 "Short permalink to this answer")

[Edit](https://tex.stackexchange.com/posts/167894/edit "Revise and improve this post")

Follow

Flag

answered Mar 26, 2014 at 21:29

[![frederik's user avatar](assets/1701949396-62a18171a2fdf4a1368c4e9616b658da.png)](https://tex.stackexchange.com/users/38437/frederik)

[frederik](https://tex.stackexchange.com/users/38437/frederik)

1,3751111 silver badges1212 bronze badges

*   [↓↓↓](# "This comment adds something useful to the post")  
      
      
      
    [↑↑↑](# "This comment adds something useful to the post")
    
    I have noted the OP question as a feature request and eventually the --flatten option of latexdiff might be updated to deal with this 'natively'. The 'null' file workaround will probably not be necessary from version 1.0.4 onwards (not yet released at the time of writing)  
    我已将 OP 问题作为功能请求，最终 latexdiff 的 --flatten 选项可能会更新以“原生”处理此问题。从 1.0.4 版开始（撰写本文时尚未发布）可能不需要“null”文件解决方法
    
    – [frederik](https://tex.stackexchange.com/users/38437/frederik "1,375 reputation")
    
    [Mar 26, 2014 at 21:30](#comment386126_167894)
    
*   [↓↓↓](# "This comment adds something useful to the post")  
      
      
      
    [↑↑↑](# "This comment adds something useful to the post")
    
    Thanks! This is an actual workaround. Although I have to copy / reference some other files not in the MWE (style, bib, ..), to make the aggregated differences-tex work, this is probably the best/easiest solution for now. (If latexdiff could do it natively, of course that would be nice, too.Thanks for latexdiff as a whole, btw :-)  
    谢谢！这是一个实际的解决方法。尽管我必须复制/引用 MWE 中没有的其他一些文件（样式、围兜等），以使聚合的差异 tex 起作用，但这可能是目前最好/最简单的解决方案。（如果 latexdiff 可以原生完成，那当然也很好。感谢整个latexdiff，顺便说一句：-）
    
    – [mfit](https://tex.stackexchange.com/users/48627/mfit "313 reputation")
    
    [Mar 30, 2014 at 8:10](#comment387501_167894)
    
*   1
    
    [↓↓↓](# "This comment adds something useful to the post")  
      
      
      
    [↑↑↑](# "This comment adds something useful to the post")
    
    Note that latexdiff version 1.0.4 is now released and --flatten supports \\subfile out of the box  
    请注意，latexdiff 版本 1.0.4 现已发布，--flatten 支持开箱即用的 \\subfile
    
    – [frederik](https://tex.stackexchange.com/users/38437/frederik "1,375 reputation")
    
    [Nov 4, 2014 at 8:18](#comment491976_167894)
    
*   1
    
    [↓↓↓](# "This comment adds something useful to the post")  
      
      
      
    [↑↑↑](# "This comment adds something useful to the post")
    
    @frederik It doesn't work if the subfile is in a subdirectory using `\def\input@path{{./tex/} {./} {../}}`.  
    @frederik 如果子文件位于使用 `\def\input@path{{./tex/} {./} {../}}` .
    
    – [Avi Ginsburg](https://tex.stackexchange.com/users/47418/avi-ginsburg "603 reputation")
    
    [Dec 30, 2015 at 10:10](#comment688530_167894)
    
*   1
    
    [↓↓↓](# "This comment adds something useful to the post")  
      
      
      
    [↑↑↑](# "This comment adds something useful to the post")
    
    @frederik Also doesn't work with `\subfile{"Some File Name"}`. Only tested on WIndows.  
    @frederik 也不适用于 `\subfile{"Some File Name"}` .仅在 Windows 上测试。
    
    – [Avi Ginsburg](https://tex.stackexchange.com/users/47418/avi-ginsburg "603 reputation")
    
    [Dec 30, 2015 at 10:42](#comment688536_167894)
    

[Add a comment](# "Use comments to ask for more information or suggest improvements. Avoid comments like “+1” or “thanks”.")

6

[↓↓↓](https://tex.stackexchange.com/posts/346316/timeline)  
  
  
  
[↑↑↑](https://tex.stackexchange.com/posts/346316/timeline)

2 years after the question was asked, but I ended up writing a batch file for solving this in a windows environment:  
在提出这个问题 2 年后，但我最终编写了一个批处理文件来在 Windows 环境中解决这个问题：

```latex
@echo off
setlocal

set "old_path=..\..\tags\old_version\my_folder\"
set "new_path=..\..\..\trunk\my_folder\"
set "doc_name=my_file.tex"

latexdiff --flatten %doc_name% %doc_name% > flat.tex
cd %old_path%
latexdiff --flatten %doc_name% %doc_name% > flat.tex
cd %new_path%
latexdiff --flatten %old_path%flat.tex flat.tex > diff.tex

rm flat.tex
rm %old_path%flat.tex
```

[Share](https://tex.stackexchange.com/a/346316/157212 "Short permalink to this answer")

[Edit](https://tex.stackexchange.com/posts/346316/edit "Revise and improve this post")

Follow

Flag

[edited Dec 30, 2016 at 2:51](https://tex.stackexchange.com/posts/346316/revisions "show all edits to this post")

answered Dec 30, 2016 at 2:21

[![Ryan B's user avatar](assets/1701949396-a8c07c6ba87aa585072fc06c831fe835.png)](https://tex.stackexchange.com/users/122016/ryan-b)

[Ryan B](https://tex.stackexchange.com/users/122016/ryan-b)

18311 silver badge55 bronze badges

[Add a comment](# "Use comments to ask for more information or suggest improvements. Avoid comments like “+1” or “thanks”.")

0

[↓↓↓](https://tex.stackexchange.com/posts/598735/timeline)  
  
  
  
[↑↑↑](https://tex.stackexchange.com/posts/598735/timeline)

Post above [link](https://tex.stackexchange.com/a/346316/243072) was very helpful, but I made my modified version that you can use.  
上面的链接非常有帮助，但我制作了您可以使用的修改版本。

```latex
@echo off
setlocal

set "old_path=..\documentation\"
set "new_path=..\documentation_old\"
set "doc_name_filename=main"

echo Generate %doc_name_filename%_flat.tex for %new_path%
cd %new_path%
latexpand %doc_name_filename%.tex > %doc_name_filename%_flat.tex

echo Generate %doc_name_filename%_flat.tex for %old_path%
cd %old_path%
latexpand %doc_name_filename%.tex > %doc_name_filename%_flat.tex

echo Generate diff
cd %new_path%
latexdiff %old_path%%doc_name_filename%_flat.tex %doc_name_filename%_flat.tex > diff.tex
pdflatex  --max-print-line=10000 -shell-escape -synctex=1 -interaction=nonstopmode -file-line-error -recorder  diff.tex 2>&1 > NUL
echo PDF generated in case of problems see diff.log

echo Cleaning up
del %doc_name_filename%_flat.tex
del %old_path%%doc_name_filename%_flat.tex

pause
```

[Share](https://tex.stackexchange.com/a/598735/157212 "Short permalink to this answer")

[Edit](https://tex.stackexchange.com/posts/598735/edit "Revise and improve this post")

Follow

Flag

answered May 26, 2021 at 20:18

[![abdarum's user avatar](assets/1701949396-04694cae0c9c73e24aec6a338cf6b9ac.png)](https://tex.stackexchange.com/users/243072/abdarum)

[abdarum](https://tex.stackexchange.com/users/243072/abdarum)

1

[Add a comment](# "Use comments to ask for more information or suggest improvements. Avoid comments like “+1” or “thanks”.")

  

## Your Answer  您的答案

*   Links
*   Images
*   Styling/Headers
*   Lists
*   Blockquotes
*   Code
*   HTML
*   Tables
*   [Advanced help](https://tex.stackexchange.com/editing-help)

Community wiki 社区维基

Post Your Answer

## 

Not the answer you're looking for? Browse other questions tagged

*   [latexdiff](https://tex.stackexchange.com/questions/tagged/latexdiff "show questions tagged 'latexdiff'")
*   [subfiles](https://tex.stackexchange.com/questions/tagged/subfiles "show questions tagged 'subfiles'")

or [ask your own question](https://tex.stackexchange.com/questions/ask).

*   The Overflow Blog  The Overflow 博客
*   [↓↓↓](https://stackoverflow.blog/2023/12/05/are-llms-the-end-of-computer-programming-as-we-know-it/?cb=1)  
      
    Are LLMs the end of computer programming (as we know it)?  
    LLM是计算机编程的终结吗？  
      
    [↑↑↑](https://stackoverflow.blog/2023/12/05/are-llms-the-end-of-computer-programming-as-we-know-it/?cb=1)
    
*   [↓↓↓](https://stackoverflow.blog/2023/12/06/behind-the-scenes-building-ibm-watsonx-an-ai-and-data-platform/?cb=1)  
      
    Behind the scenes building IBM watsonx, an AI and data platform  
    构建 IBM watsonx（AI 和数据平台）的幕后花絮  
      
    [↑↑↑](https://stackoverflow.blog/2023/12/06/behind-the-scenes-building-ibm-watsonx-an-ai-and-data-platform/?cb=1)
    
    sponsored post 赞助帖子
    
*   Featured on Meta  Meta 精选
*   [↓↓↓](https://meta.stackexchange.com/questions/395062/seeking-feedback-on-tag-colors-update?cb=1)  
      
    Seeking feedback on tag colors update  
    寻求有关标签颜色更新的反馈  
      
    [↑↑↑](https://meta.stackexchange.com/questions/395062/seeking-feedback-on-tag-colors-update?cb=1)
    
*   [↓↓↓](https://meta.stackexchange.com/questions/395198/site-maintenance-wednesday-december-13-2023-0100-utc-tuesday-december-1?cb=1 "Site maintenance - Wednesday, December 13, 2023 @ 01:00 UTC (Tuesday, December 12 @ 8:00 pm EST)")  
      
    Site maintenance - Wednesday, December 13, 2023 @ 01:00 UTC (Tuesday,...  
    网站维护 - 2023 年 12 月 13 日星期三 @ 01：00 UTC（星期二,...  
      
    [↑↑↑](https://meta.stackexchange.com/questions/395198/site-maintenance-wednesday-december-13-2023-0100-utc-tuesday-december-1?cb=1 "Site maintenance - Wednesday, December 13, 2023 @ 01:00 UTC (Tuesday, December 12 @ 8:00 pm EST)")
    

#### Linked 联系

[112](https://tex.stackexchange.com/q/21838?lq=1 "Question score (upvotes - downvotes)")

[↓↓↓](https://tex.stackexchange.com/questions/21838/replace-inputfilex-by-the-content-of-filex-automatically?noredirect=1&lq=1)  
  
Replace \\input{fileX} by the content of fileX automatically  
自动将 \\input{fileX} 替换为 fileX 的内容  
  
[↑↑↑](https://tex.stackexchange.com/questions/21838/replace-inputfilex-by-the-content-of-filex-automatically?noredirect=1&lq=1)

#### Related 相关

[19](https://tex.stackexchange.com/q/61405?rq=1 "Question score (upvotes - downvotes)")

[↓↓↓](https://tex.stackexchange.com/questions/61405/latexdiff-svn-not-working-with-multiple-files-flatten?rq=1)  
  
latexdiff + svn not working with multiple files (flatten)  
LaTeXdiff + SVN 无法处理多个文件（展平）  
  
[↑↑↑](https://tex.stackexchange.com/questions/61405/latexdiff-svn-not-working-with-multiple-files-flatten?rq=1)

[3](https://tex.stackexchange.com/q/229150?rq=1 "Question score (upvotes - downvotes)")

[↓↓↓](https://tex.stackexchange.com/questions/229150/subfiles-in-subdirectory-file-not-found?rq=1)  
  
Subfiles in subdirectory, file not found  
子目录中的子文件，找不到文件  
  
[↑↑↑](https://tex.stackexchange.com/questions/229150/subfiles-in-subdirectory-file-not-found?rq=1)

[0](https://tex.stackexchange.com/q/305021?rq=1 "Question score (upvotes - downvotes)")

[↓↓↓](https://tex.stackexchange.com/questions/305021/using-chapterbib-subfiles-achemso?rq=1)  
  
Using Chapterbib + subfiles + achemso  
使用 Chapterbib + 子文件 + achemso  
  
[↑↑↑](https://tex.stackexchange.com/questions/305021/using-chapterbib-subfiles-achemso?rq=1)

[4](https://tex.stackexchange.com/q/385200?rq=1 "Question score (upvotes - downvotes)")

[↓↓↓](https://tex.stackexchange.com/questions/385200/file-path-problems-using-subfiles-package?rq=1)  
  
File path problems using subfiles package  
使用子文件包的文件路径问题  
  
[↑↑↑](https://tex.stackexchange.com/questions/385200/file-path-problems-using-subfiles-package?rq=1)

[1](https://tex.stackexchange.com/q/478460?rq=1 "Question score (upvotes - downvotes)")

[↓↓↓](https://tex.stackexchange.com/questions/478460/main-bibliography-at-the-end-of-the-main-document-and-at-the-end-of-the-subfiles?rq=1)  
  
Main bibliography at the end of the main document and at the end of the subfiles  
主文档末尾和子文件末尾的主要参考书目  
  
[↑↑↑](https://tex.stackexchange.com/questions/478460/main-bibliography-at-the-end-of-the-main-document-and-at-the-end-of-the-subfiles?rq=1)

[3](https://tex.stackexchange.com/q/585861?rq=1 "Question score (upvotes - downvotes)")

[↓↓↓](https://tex.stackexchange.com/questions/585861/understanding-how-cross-referencing-latex-projects-with-subfiles?rq=1)  
  
Understanding how cross-referencing LaTeX projects with subfiles  
了解如何使用子文件交叉引用 LaTeX 项目  
  
[↑↑↑](https://tex.stackexchange.com/questions/585861/understanding-how-cross-referencing-latex-projects-with-subfiles?rq=1)

[0](https://tex.stackexchange.com/q/594770?rq=1 "Question score (upvotes - downvotes)")

[↓↓↓](https://tex.stackexchange.com/questions/594770/overleaf-word-count-grossly-undercounting-with-subfiles-and-input?rq=1)  
  
Overleaf Word Count grossly undercounting with Subfiles and Input  
Overleaf 字数严重不足，包含子文件和输入  
  
[↑↑↑](https://tex.stackexchange.com/questions/594770/overleaf-word-count-grossly-undercounting-with-subfiles-and-input?rq=1)

[1](https://tex.stackexchange.com/q/612279?rq=1 "Question score (upvotes - downvotes)")

[↓↓↓](https://tex.stackexchange.com/questions/612279/possible-subfiles-setspace-issues?rq=1)  
  
Possible subfiles/setspace issues  
可能的子文件/设置空间问题  
  
[↑↑↑](https://tex.stackexchange.com/questions/612279/possible-subfiles-setspace-issues?rq=1)

#### 

[↓↓↓](https://stackexchange.com/questions?tab=hot)  
  
Hot Network Questions  
网络热点问题  
  
[↑↑↑](https://stackexchange.com/questions?tab=hot)

*   [↓↓↓](https://german.stackexchange.com/questions/75902/how-does-one-express-the-ordering-of-thoughts)  
      
    How does one express the ordering of thoughts?  
    如何表达思想的顺序？  
      
    [↑↑↑](https://german.stackexchange.com/questions/75902/how-does-one-express-the-ordering-of-thoughts)
    
*   [↓↓↓](https://mathoverflow.net/questions/459908/cardinality-of-subset-of-pa-that-contains-all-the-sets-with-lesser-cardinality)  
      
    Cardinality of subset of P(A) that contains all the sets with lesser cardinality than A  
    P（A） 子集的基数，包含基数小于 A 的所有集合  
      
    [↑↑↑](https://mathoverflow.net/questions/459908/cardinality-of-subset-of-pa-that-contains-all-the-sets-with-lesser-cardinality)
    
*   [↓↓↓](https://workplace.stackexchange.com/questions/194568/how-do-i-show-employers-that-a-long-commute-wont-hinder-my-ability-to-perform-m)  
      
    How do I show employers that a long commute won't hinder my ability to perform my assigned duties?  
    我如何向雇主表明，长途通勤不会妨碍我履行分配的职责？  
      
    [↑↑↑](https://workplace.stackexchange.com/questions/194568/how-do-i-show-employers-that-a-long-commute-wont-hinder-my-ability-to-perform-m)
    
*   [↓↓↓](https://mathoverflow.net/questions/459740/what-is-the-minimal-density-of-a-set-a-such-that-aa-n)  
      
    What is the minimal density of a set A such that A+A = N?  
    集合 A 的最小密度是多少，使得 A+A = N？  
      
    [↑↑↑](https://mathoverflow.net/questions/459740/what-is-the-minimal-density-of-a-set-a-such-that-aa-n)
    
*   [↓↓↓](https://superuser.com/questions/1819651/how-do-i-reset-file-ownership-at-the-command-line-when-the-files-are-owned-by-us)  
      
    How do I reset file ownership at the command line when the files are owned by users from a dead domain?  
    当文件归失效域中的用户所有时，如何在命令行中重置文件所有权？  
      
    [↑↑↑](https://superuser.com/questions/1819651/how-do-i-reset-file-ownership-at-the-command-line-when-the-files-are-owned-by-us)
    
*   [↓↓↓](https://worldbuilding.stackexchange.com/questions/251651/can-a-spaceship-hitchhike-on-an-explosion-to-escape-a-gravity-well)  
      
    Can a spaceship "hitchhike" on an explosion to escape a gravity well?  
    宇宙飞船能否在爆炸中“搭便车”以逃避重力井？  
      
    [↑↑↑](https://worldbuilding.stackexchange.com/questions/251651/can-a-spaceship-hitchhike-on-an-explosion-to-escape-a-gravity-well)
    
*   [↓↓↓](https://judaism.stackexchange.com/questions/138720/do-angels-still-manifest-themselves-as-humans-and-appear-to-us-unknowingly)  
      
    Do angels still manifest themselves as humans and appear to us unknowingly?  
    天使是否仍然以人类的身份显现，并在不知不觉中出现在我们面前？  
      
    [↑↑↑](https://judaism.stackexchange.com/questions/138720/do-angels-still-manifest-themselves-as-humans-and-appear-to-us-unknowingly)
    
*   [↓↓↓](https://skeptics.stackexchange.com/questions/56429/did-cornelius-vanderbilts-descendants-lose-their-family-wealth-by-1973)  
      
    Did Cornelius Vanderbilt's descendants lose their family wealth by 1973?  
    科尼利厄斯·范德比尔特的后代在 1973 年之前失去了家族财富吗？  
      
    [↑↑↑](https://skeptics.stackexchange.com/questions/56429/did-cornelius-vanderbilts-descendants-lose-their-family-wealth-by-1973)
    
*   [↓↓↓](https://mathoverflow.net/questions/459890/closed-formula-for-number-of-ones-in-a-proper-factor-tree)  
      
    Closed formula for number of ones in a proper factor tree  
    适当因子树中 1 数的闭合公式  
      
    [↑↑↑](https://mathoverflow.net/questions/459890/closed-formula-for-number-of-ones-in-a-proper-factor-tree)
    
*   [↓↓↓](https://blender.stackexchange.com/questions/306441/how-to-project-a-vertex-to-the-nearest-point-along-a-vector)  
      
    How to project a vertex to the nearest point along a vector?  
    如何将顶点投影到向量上最近的点？  
      
    [↑↑↑](https://blender.stackexchange.com/questions/306441/how-to-project-a-vertex-to-the-nearest-point-along-a-vector)
    
*   [↓↓↓](https://academia.stackexchange.com/questions/204663/accepted-postdoc-offer-retracted-last-minute)  
      
    Accepted postdoc offer retracted last minute  
    接受的博士后录取通知书在最后一刻被撤回  
      
    [↑↑↑](https://academia.stackexchange.com/questions/204663/accepted-postdoc-offer-retracted-last-minute)
    
*   [↓↓↓](https://scifi.stackexchange.com/questions/281519/identifying-an-actor-in-star-wars-a-new-hopes-tantive-iv-boarding-scene)  
      
    Identifying an Actor in Star Wars: A New Hope's Tantive IV Boarding Scene?  
      
    [↑↑↑](https://scifi.stackexchange.com/questions/281519/identifying-an-actor-in-star-wars-a-new-hopes-tantive-iv-boarding-scene)
    
*   [↓↓↓](https://ell.stackexchange.com/questions/344998/cat-has-a-final-t-the-letter-t-is-the-only-one-in-the-word-cat-then)  
      
    'Cat' has a final 't'. — The letter "t" is the only one in the word "cat". Then why is it possible to use "a" here?  
      
    [↑↑↑](https://ell.stackexchange.com/questions/344998/cat-has-a-final-t-the-letter-t-is-the-only-one-in-the-word-cat-then)
    
*   [↓↓↓](https://stats.stackexchange.com/questions/633205/can-i-use-p-values-without-hypothesis)  
      
    Can I use p-values without hypothesis?  
      
    [↑↑↑](https://stats.stackexchange.com/questions/633205/can-i-use-p-values-without-hypothesis)
    
*   [↓↓↓](https://philosophy.stackexchange.com/questions/105961/is-it-unscientific-to-be-sceptical-without-offering-alternative-explanations)  
      
    Is it "unscientific" to be sceptical without offering alternative explanations?  
      
    [↑↑↑](https://philosophy.stackexchange.com/questions/105961/is-it-unscientific-to-be-sceptical-without-offering-alternative-explanations)
    
*   [↓↓↓](https://hsm.stackexchange.com/questions/15998/what-was-the-role-of-schmidt-in-derivation-of-the-gram-schmidt-process)  
      
    What was the role of Schmidt in derivation of the Gram-Schmidt process?  
      
    [↑↑↑](https://hsm.stackexchange.com/questions/15998/what-was-the-role-of-schmidt-in-derivation-of-the-gram-schmidt-process)
    
*   [↓↓↓](https://german.stackexchange.com/questions/75888/are-there-any-kausal-and-modal-prepositions-in-german)  
      
    Are there any Kausal and Modal prepositions in German?  
      
    [↑↑↑](https://german.stackexchange.com/questions/75888/are-there-any-kausal-and-modal-prepositions-in-german)
    
*   [↓↓↓](https://codegolf.stackexchange.com/questions/267313/can-the-chefs-go)  
      
    Can the chefs go?  
      
    [↑↑↑](https://codegolf.stackexchange.com/questions/267313/can-the-chefs-go)
    
*   [↓↓↓](https://music.stackexchange.com/questions/132933/what-is-this-quadruple-dotted-x-above-the-staff)  
      
    What is this quadruple-dotted X above the staff?  
      
    [↑↑↑](https://music.stackexchange.com/questions/132933/what-is-this-quadruple-dotted-x-above-the-staff)
    
*   [↓↓↓](https://gaming.stackexchange.com/questions/405380/does-becoming-a-warlock-mean-said-warlock-will-become-a-soul-coin-upon-death)  
      
    Does becoming a warlock mean said warlock will become a "Soul Coin" upon death?  
      
    [↑↑↑](https://gaming.stackexchange.com/questions/405380/does-becoming-a-warlock-mean-said-warlock-will-become-a-soul-coin-upon-death)
    
*   [↓↓↓](https://worldbuilding.stackexchange.com/questions/251696/can-we-hit-the-spaceship)  
      
    Can we hit the spaceship  
      
    [↑↑↑](https://worldbuilding.stackexchange.com/questions/251696/can-we-hit-the-spaceship)
    
*   [↓↓↓](https://ell.stackexchange.com/questions/345002/climbing-without-moving-how-do-you-say-that)  
      
    Climbing without moving, how do you say that?  
      
    [↑↑↑](https://ell.stackexchange.com/questions/345002/climbing-without-moving-how-do-you-say-that)
    
*   [↓↓↓](https://japanese.stackexchange.com/questions/101925/does-kanji-have-meaning-on-their-own-or-they-inherit-their-meanings-from-the)  
      
    Does kanji have meaning on their own, or they inherit their meaning(s) from the words they used in?  
      
    [↑↑↑](https://japanese.stackexchange.com/questions/101925/does-kanji-have-meaning-on-their-own-or-they-inherit-their-meanings-from-the)
    
*   [↓↓↓](https://chemistry.stackexchange.com/questions/178155/does-distance-exist-in-thermodynamic-coordinates)  
      
    Does distance exist in thermodynamic coordinates?  
      
    [↑↑↑](https://chemistry.stackexchange.com/questions/178155/does-distance-exist-in-thermodynamic-coordinates)
    

[↓↓↓](https://tex.stackexchange.com/feeds/question/167620 "Feed of this question and its answers")  
  
Question feed  
  
[↑↑↑](https://tex.stackexchange.com/feeds/question/167620 "Feed of this question and its answers")
