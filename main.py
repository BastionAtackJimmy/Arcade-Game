sprite1 = sprites.create(img("""
        . . . . . . . c d . . . . . . . 
            . . . . . . . c d . . . . . . . 
            . . . . . . . c d . . . . . . . 
            . . . . . . . c b . . . . . . . 
            . . . . . . . f f . . . . . . . 
            . . . . . . . c 4 . . . . . . . 
            . . . . . . . f f . . . . . . . 
            . . . . . . . e 4 . . . . . . . 
            . . . . . . e e 5 2 . . . . . . 
            . . . . . . e 4 5 2 . . . . . . 
            . . . . . c c c 2 2 2 . . . . . 
            . . . . e e 4 4 4 5 2 2 . . . . 
            . . e f f f c c 2 2 f f 2 2 . . 
            . e e e e 2 2 4 4 4 4 5 4 2 2 . 
            e e e e e e 2 2 4 4 4 5 4 4 2 2 
            e e e e e e 2 2 4 4 4 4 5 4 2 2
    """),
    SpriteKind.player)
sprite1.set_position(75, 50)

def on_forever():
    controller.move_sprite(sprite1, 100, 100)
forever(on_forever)
