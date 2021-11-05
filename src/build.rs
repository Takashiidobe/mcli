use man::prelude::*;
use std::fs::File;
use std::io::{Error, Write};

fn main() -> Result<(), Error> {
    let path = "mcli.1";
    let mut output = File::create(path)?;

    let msg = Manual::new("mcli")
        .about("A music player cli in rust.")
        .arg(Arg::new("path"))
        .custom(Section::new("commands").paragraph(
            r#"
v      Volume. Set the volume.

        "#,
        ))
        .author(Author::new("Takashi I").email("mail@takashiidobe.com"))
        .render();

    write!(output, "{}", msg)
}
