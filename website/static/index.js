function delete_note(noteID){
    fetch('/delete-note',{
        method: 'POST',
        body: JSON.stringify({ noteID: noteID})
    }).then((_res) => {
        window.location.href = "/";
    })
}

function delete_all_notes(userID){
    fetch('/delete-all-notes',{
        method: 'POST',
        body: JSON.stringify({ userID: userID})
    }).then((_res) => {
        window.location.href = "/";
    })
}