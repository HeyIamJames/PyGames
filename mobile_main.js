<!doctype html>
<html><head><script src="enchant.js"></script></head>
<body style="margin:0; padding: 0;">
<script>
    enchant(); // initialize
    var game = new Core(320, 320); // game stage
    game.preload('chara1.png'); // preload image
    game.fps = 20;

    game.onload = function(){
        var bear = new Sprite(32, 32);
        bear.image = game.assets['chara1.png'];
        game.rootScene.addChild(bear);
        bear.frame = [6, 6, 7, 7];   
        
        bear.tl.moveBy(288, 0, 90)   
            .scaleTo(-1, 1, 10)      
            .moveBy(-288, 0, 90)     
            .scaleTo(1, 1, 10)       
            .loop();                
    };

    game.start(); // start your game!
</script>
</body>
</html>
