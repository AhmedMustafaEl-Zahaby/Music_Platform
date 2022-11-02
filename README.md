## Task

We don't want all albums to be put up for sale immediately, first we want to make sure the album name is suitable for out platform, for example
the album name shouldn't contain inappropriate expressions.

1. Add a boolean field to the album model that will help us represent whether an album is approved by an admin or not
   - tip: follow the convention for boolean field names
   - hint: what's the suitable default value for this field, (`True` or `False`)?
2. Add all models you have so far to django admin
3. The admin shouldn't be able to modify the creation time field on the album (this field should be in read-only status on django admin)
4. Add a help text that would show up under the previously mentioned boolean field on the django admin form, it should state:
   - > Approve the album if its name is not explicit
   - bonus: can you add the help text without modifying the boolean field itself? (hint: you'll modify the form)
5. When viewing the list of artists, there must be a column to show the number of approved albums for each artist
6. (bonus) Modify the artist queryset so that I can order the list of artists by the number of their approved albums
   - I should be able to do the following `Artist.objects.....order_by("approved_albums")`
7. Allow the admin to create albums for the artist from from the artist's editing form
