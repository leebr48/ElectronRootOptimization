I am not very good with MatLab, so I make the following note:

If you wish to produce the PDF from the `.fig` file, you must first open the `.fig` in MatLab to make it the "active figure" and then run

`print('opt_Bmid', '-dpdf', '-bestfit')`.

To trim off the extra white space, run

`pdf-crop-margins -p 0 opt_Bmid.pdf`.

Finally, rename the cropped file by running

`mv opt_Bmid_cropped.pdf opt_Bmid.pdf'.
