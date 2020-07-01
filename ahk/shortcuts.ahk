; Prompt user to take a screenshot and save to 
; dbtools_jpc.constants.local_images_path
^!;::

  env = C:\.dropbox\Scripts\activate
  pycommand := "from dbtools_jpc.screensnip import take; take()"
  run, %comspec% /c %env% & python -c "%pycommand%"

return

; Get the direct url of the most recently modifed image in 
; Dropbox\images
^!'::
  env = C:\.dropbox\Scripts\activate
  pycommand := "from dbtools_jpc.image import recently_modified_link; recently_modified_link()"
  run, %comspec% /c %env% & python -c "%pycommand%"

return
