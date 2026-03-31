<script>
       window.isValidImage = (file) => {
           const validTypes = ['image/jpeg', 'image/png', 'image/webp', 'image/heic'];
           if (!validTypes.includes(file.type)) {
               alert(`File ${file.name} is not a supported image.`);
               return false;
           }
           return true;
       };
   </script>


