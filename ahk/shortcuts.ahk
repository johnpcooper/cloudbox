; Prompt user to take a screenshot and save to 
; cloudbox.constants.local_images_path
^!;::

  env = C:\.dropbox\Scripts\activate
  pycommand := "from cloudbox.screensnip import take; take()"
  run, %comspec% /c %env% & python -c "%pycommand%"

return

; Get the direct url of the most recently modifed image in 
; Dropbox\images
^!'::
  env = C:\.dropbox\Scripts\activate
  pycommand := "from cloudbox.image import recently_modified_link; recently_modified_link()"
  run, %comspec% /c %env% & python -c "%pycommand%"

return
