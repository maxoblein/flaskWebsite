function delete_note(noteID){
    fetch('/delete-note',{
        method: 'POST',
        body: JSON.stringify({ noteID: noteID})
    }).then((_res) => {
        window.location.href = "/";
    })
}