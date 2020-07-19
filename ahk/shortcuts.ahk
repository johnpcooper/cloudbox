; Prompt user to take a screenshot and save to 
; cloudbox.constants.local_images_path
^!;::

  env = C:\.cloudbox\Scripts\activate
  pycommand := "from cloudbox.screensnip import take; take()"
  run, %comspec% /c %env% & python -c "%pycommand%"

return

; Get the direct url of the most recently modifed image in 
; cloudbox\images and put it on the clipboard for 5 seconds. 
; Takes about 1 s to get the url (cloudbox/image.py for more
; details)
^!'::
  env = C:\.cloudbox\Scripts\activate
  pycommand := "from cloudbox.image import recently_modified_link; recently_modified_link()"
  run, %comspec% /c %env% & python -c "%pycommand%"

return

; Write clipboard to a new note. If file with
; auto generate filename exists, append to that
; file
^!/::
  env = C:\.cloudbox\Scripts\activate
  pycommand := "from cloudbox.text import write_note_from_clipboard; from time import sleep; write_note_from_clipboard(); sleep(5)"
  run, %comspec% /c %env% & python -c "%pycommand%"

return