const fs = require('fs')
const Bleacon = require('bleacon');
const uuid = 'aaaaaaaabbbbccccddddeeeeeeeeeeee'; // 本来は、列車を識別する
const measuredPower = -59;

Bleacon.startScanning(uuid);
Bleacon.on('discover', function(bleacon) {
   console.log(bleacon);
});

setInterval(function(){
    Bleacon.stopAdvertising();
    //ファイルを取得
    try {
        let conjestion = fs.readFileSync("../log.txt", 'utf-8');
        console.log(conjestion);
        let terms = conjestion.split(',');
        let major = Number(terms[0] + terms[1] + terms[2]);
        let minor = Number(terms[3]);
        Bleacon.startAdvertising(uuid, major, minor, measuredPower);
    }catch(e) {
        //console.log("log.txtがありません");
    }
}, 5000)

