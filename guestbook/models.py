from django.db import models

class Comments(models.Model):
    text = models.CharField(max_length=400)
    nickname = models.CharField(max_length=12)
    pub_date = models.DateTimeField('date', auto_now=False, auto_now_add=True)
    
    def __unicode__(self):
        return self.text
    
    def textstart(self):
        words = self.text.split(" ")
        tstart = ""
        i = 0
        if (len(words) < 20):
            return self.text
        else:
            for word in words:
                if (i > 20):
                    break
                i = i + 1
                tstart = tstart + word + " "
            return tstart 
        #return self.text[:20]