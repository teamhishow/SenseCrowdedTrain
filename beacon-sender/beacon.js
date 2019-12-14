const fs = require('fs')
const Bleacon = require('bleacon');
const uuid = 'aaaaaaaabbbbccccddddeeeeeeeeeeee'; // 本来は、列車を識別する
const major = 12;
const measuredPower = -59;

Bleacon.startScanning(uuid);
Bleacon.on('discover', function(bleacon) {
   console.log(bleacon);
});

setInterval(function(){
    Bleacon.stopAdvertising();
    //ファイルを取得
    let conjestion = fs.readFileSync("../log.txt", 'utf-8');
    conjestion = parseInt(conjestion);
    console.log("混雑度: " + conjestion)
    Bleacon.startAdvertising(uuid, major, conjestion, measuredPower);
}, 5000)

