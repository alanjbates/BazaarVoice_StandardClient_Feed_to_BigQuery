import pysftp
from fs_gcsfs import GCSFS
import datetime

#set gcs params
target_bucket_name = 'your-GCS-bucket-name-here'
gcsfs = GCSFS(bucket_name=target_bucket_name)

#set ftp params
cnopts = pysftp.CnOpts()
cnopts.hostkeys = 'known_hosts'

sftp = pysftp.Connection('sftp.your_host_here.com',
                     username='your_username_here',
                     password='your_password_here',
                        cnopts=cnopts)

# get files within the root directory into list
filenames = sftp.listdir("path/")
filenames_attr = sftp.listdir_attr("path/")

#copy file into gcs
for filename in filenames_attr:
    if 'thefileyouarelookingfor.xml.gz' in filename.filename:
        file_dttm = datetime.datetime.utcfromtimestamp(file.st_atime).strftime("%Y%m%d_%H%M%S")
        gcs_target_filename = 'thefileyouarelookingfor_' + file_dttm + '.xml.gz'
        print('Retrieving file: ' + gcs_target_filename)
        sftp.getfo("feeds/" + fileattr.filename, gcsfs.open(gcs_target_filename, 'wb'))
        print('Successfully created: ' + gcs_target_filename)
    else:
        print('No standard client feed found in remote host feeds/ folder.')

#close ftp connection
sftp.close()
