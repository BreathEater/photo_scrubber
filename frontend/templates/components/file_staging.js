<script>
       window.fileStaging = {
           queue: [],
	add(newFiles) {
	       Array.from(newFiles).forEach(file => {

		   if (!window.isValidImage(file)) return;

                   if (!this.queue.find(f => f.name === file.name && f.size === file.size)) {
                       this.queue.push(file);
                   }
               });
               document.dispatchEvent(new CustomEvent('stager-updated'));
           },
           remove(index) {
               this.queue.splice(index, 1);
               document.dispatchEvent(new CustomEvent('stager-updated'));
           },
           clear() {
               this.queue = [];
               document.dispatchEvent(new CustomEvent('stager-updated'));
           }
       };
   </script>

