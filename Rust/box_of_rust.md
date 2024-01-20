# Box of rust

## 问题引入

```rust
Struct Circle {
    radius: f64,
}

Struct Square {
    side: f64,
}

trait Drawable {
    fn draw(&self);
}

impl Drawable for Circle {
    fn draw(&self) {
        println!("Drawing a circle with radius {}", self.radius);
    }
}

impl Drawable for Square {
    fn draw(&self) {
        println!("Drawing a square with side {}", self.side);
    }
}
```

现在我们有一个`Vec`，里面存放了`Circle`和`Square`的实例，我们想要调用`draw`方法，该怎么做呢？

```rust
fn main() {
    let shapes: Vec<Box<dyn Drawable>> = vec![
        Box::new(Circle { radius: 1.0 }),
        Box::new(Square { side: 1.0 }),
    ];

    for shape in &shapes {
        shape.draw();
    }
}
```

这里的`shape`的类型是`&Box<dyn Drawable>`，而不是`&dyn Drawable`。

```rust
    let circ_box = Box::new(Circle { radius: 1.0 });
    let circ = *circ_box;
    circ.draw();
```

是可以编译通过的，因为可以推断出`circ`的类型是`Circle`，而`Circle`实现了`Drawable`，所以可以调用`draw`方法。

```rust
    let squr_box = &shapes[1];
    squr_box.draw();
```

也是可以编译通过的，因为`squr_box`的类型是`&Box<dyn Drawable>`，而Box实现了`Deref`，所以可以调用`draw`方法。

```rust
    let squr = *squr_box;
    squr.draw();
```

这里就会报错，因为`squr_box`的类型是`&Box<dyn Drawable>`，而`Box`没有实现`Copy`，所以不能解引用。

那么实现一个`clone_box`方法会如何呢？

```rust
trait Drawable {
    fn draw(&self);
    fn clone_box(&self) -> Box<dyn Drawable>;
    // 在 Drawable trait 中添加 clone_box 方法
}

struct DrawableBox {
    inside: Box<dyn Drawable>,
    // 定义一个 DrawableBox 结构体，里面包含一个 Box<dyn Drawable> 类型的成员
}

impl Clone for DrawableBox {
    fn clone(&self) -> Self {
        DrawableBox {
            inside: self.inside.clone_box(),
        }
    }
    // 为 DrawableBox 实现 Clone trait
}

impl Drawable for DrawableBox {
    fn draw(&self) {
        self.inside.draw();
    }
    fn clone_box(&self) -> Box<dyn Drawable> {
        Box::new(self.clone())
    }
}

#[derive(Clone)]
struct Circle {
    radius: f64,
}

impl Drawable for Circle {
    fn draw(&self) {
        println!("Drawing a circle with radius {}", self.radius);
    }
    fn clone_box(&self) -> Box<dyn Drawable> {
        Box::new(self.clone())
    }
}

#[derive(Clone)]
struct Square {
    side: f64,
}

impl Drawable for Square {
    fn draw(&self) {
        println!("Drawing a square with side {}", self.side);
    }
    fn clone_box(&self) -> Box<dyn Drawable> {
        Box::new(self.clone())
    }
}

fn main() {
    let shapes: Vec<Box<dyn Drawable>> = vec![
        Box::new(Circle { radius: 1.0 }),
        Box::new(Square { side: 2.0 }),
    ];

    for shape in &shapes {
        shape.draw();
    }

    println!("Dereferencing a Box");
    let circ_box = Box::new(Circle { radius: 1.0 });
    let circ = *circ_box;
    println!("Radius: {}", circ.radius);

    let squr_box = &shapes[1];
    let squr_drawable_box = DrawableBox {
        inside: squr_box.clone_box(),
    };
    let squr_clone = squr_drawable_box.clone();
    squr_clone.draw();

    let squr = *squr_drawable_box.inside;
}
```

```log
error[E0277]: the size for values of type `dyn Drawable` cannot be known at compilation time
  --> src/main.rs:85:9
   |
85 |     let squr = *squr_drawable_box.inside;
   |         ^^^^ doesn't have a size known at compile-time
   |
   = help: the trait `Sized` is not implemented for `dyn Drawable`
   = note: all local variables must have a statically known size
   = help: unsized locals are gated as an unstable feature
```

可以看见，就算`Box`实现了`Copy`，也会报错，因为编译器不知道`squr`的类型是`Square`，还是`Circle`，无法在编译期确定内存大小。

不过这里的`clone_box`方法，可以用于dyn Drawable 的 deepcopy, 想实现的逻辑是可以这么实现的。

```rust
trait Drawable {
    fn draw(&self);
    fn clone_box(&self) -> Box<dyn Drawable>;
    fn get_center(&self) -> (f64, f64);
    fn set_center(&mut self, center: (f64, f64));
}

struct DrawableBox {
    inside: Box<dyn Drawable>,
}

// impl DrawableBox {
//     fn new<T: Drawable + 'static>(drawable: T) -> DrawableBox {
//         DrawableBox {
//             inside: Box::new(drawable),
//         }
//     }
// }

impl Clone for DrawableBox {
    fn clone(&self) -> Self {
        DrawableBox {
            inside: self.inside.clone_box(),
        }
    }
}

impl Drawable for DrawableBox {
    fn draw(&self) {
        self.inside.draw();
    }
    fn clone_box(&self) -> Box<dyn Drawable> {
        Box::new(self.clone())
    }
    fn get_center(&self) -> (f64, f64) {
        self.inside.get_center()
    }
    fn set_center(&mut self, center: (f64, f64)) {
        self.inside.set_center(center);
    }
}

#[derive(Clone)]
struct Circle {
    radius: f64,
    center: (f64, f64),
}

impl Drawable for Circle {
    fn draw(&self) {
        println!("Drawing a circle with radius {}", self.radius);
        println!("Center: {:?}", self.center);
    }
    fn clone_box(&self) -> Box<dyn Drawable> {
        Box::new(self.clone())
    }
    fn get_center(&self) -> (f64, f64) {
        self.center
    }
    fn set_center(&mut self, center: (f64, f64)) {
        self.center = center;
    }
}

#[derive(Clone)]
struct Square {
    side: f64,
    center: (f64, f64),
}

impl Drawable for Square {
    fn draw(&self) {
        println!("Drawing a square with side {}", self.side);
        println!("Center: {:?}", self.center);
    }
    fn clone_box(&self) -> Box<dyn Drawable> {
        Box::new(self.clone())
    }
    fn get_center(&self) -> (f64, f64) {
        self.center
    }
    fn set_center(&mut self, center: (f64, f64)) {
        self.center = center;
    }
}

fn main() {
    let mut shapes: Vec<Box<dyn Drawable>> = vec![
        Box::new(Circle { radius: 1.0, center: (0.0, 0.0) }),
        Box::new(Square { side: 1.0, center: (0.0, 0.0) }),
    ];

    for shape in &shapes {
        shape.draw();
    }

    println!("Dereferencing a Box");
    let circ_box = Box::new(Circle { radius: 2.0 , center: (1.0, 1.0) });
    let circ = *circ_box;
    println!("Radius: {}", circ.radius);

    let squr_box = &shapes[1];
    let mut squr_drawable_box = DrawableBox {
        inside: squr_box.clone_box(),
    };

    shapes[1].set_center((2.0, 1.0));
    shapes[1].draw();
    squr_drawable_box.set_center((1.0, 2.0));
    squr_drawable_box.draw();
    // change 
}
```

```log
Drawing a circle with radius 1
Center: (0.0, 0.0)
Drawing a square with side 1
Center: (0.0, 0.0)
Dereferencing a Box
Radius: 2
Drawing a square with side 1
Center: (2.0, 1.0)
Drawing a square with side 1
Center: (1.0, 2.0)
```

可以看见，`squr_drawable_box`和`shapes[1]`的`center`是不一样的，这就实现了deepcopy。
