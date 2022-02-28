"""
create a unique instance for the application

import the file file storage and use the method reload in the FileStorage class.
"""


from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
