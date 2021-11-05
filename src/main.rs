use rustyline::Editor;

use rodio::Sink;
use std::fs::File;
use std::io::BufReader;

fn main() {
    let (_stream, stream_handle) = rodio::OutputStream::try_default().unwrap();
    let sink = Sink::try_new(&stream_handle).unwrap();
    sink.set_volume(0.5);

    let mut rl = Editor::<()>::new();
    if rl.load_history("history.txt").is_err() {
        println!("No previous history.");
    }

    loop {
        let readline = rl.readline(">> ");
        match readline {
            Ok(line) => {
                rl.add_history_entry(line.as_str());
                if line.starts_with("v") {
                    let mut volume: f32 = line[1..].trim().parse().unwrap();
                    volume = if volume > 1.0 { 1.0 } else { volume };
                    volume = if volume < 0.0 { 0.0 } else { volume };
                    sink.set_volume(volume);
                    continue;
                }
                if line.starts_with("volume") {
                    let mut volume: f32 = line[6..].trim().parse().unwrap();
                    volume = if volume > 1.0 { 1.0 } else { volume };
                    volume = if volume < 0.0 { 0.0 } else { volume };
                    sink.set_volume(volume);
                    continue;
                }
                let file = File::open(&line);
                if let Ok(file) = file {
                    let source = rodio::Decoder::new(BufReader::new(file));
                    if let Ok(source) = source {
                        sink.append(source);
                    } else {
                        println!("The file was not valid to play. Try again.");
                    }
                } else {
                    println!("No such file found. Try again.");
                }
            }
            Err(_) => {
                println!("Exiting.");
                break;
            }
        }
    }
    rl.save_history("history.txt").unwrap();
}
