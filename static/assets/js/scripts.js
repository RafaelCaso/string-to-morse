//$(document).ready(() => {
//    const storage = firebase.storage();
//
//    $(".encode").click(async () => {
//        const file = await getFile("output.mp3");
//        playFile(file)
//    })
//
//    async function getFile(fileName) {
//        const gsRef =storage.refFromURL("gs://morse-4a61c.appspot.com/output.mp3");
//        const url = await gsRef.getDownloadURL();
//        return url
//    }
//
//    function playFile(file) {
//        $(".audio-controls").attr("src", file).attr("autoplay", true);
//    }
//})


// SPAEBAR AS MORSE ENCODER
//$(document).ready(() => {
//  $(".encode").click( async () => {
//      $(".audio").attr("src", "output.mp3").attr("autoplay", true)
//  })
//
//
//
//
//  $('body').keyup(function(e){
//  var ditAudioElement = document.createElement('audio');
//  ditAudioElement.setAttribute('src', "/static/sound/dit.mp3")
//
//  var dahAudioElement = document.createElement('audio');
//  dahAudioElement.setAttribute('src', "/static/sound/dah.mp3")
//
//      if(e.keyCode == 32){
//      $("h2").append("-")
//      dahAudioElement.play()
//      }
//    })
//  })