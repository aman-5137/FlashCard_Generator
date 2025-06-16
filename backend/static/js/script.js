let flashcards = [];
  let currentIndex = 0;
  const flashcard = document.getElementById("flashcard");
  const cardFront = document.getElementById("cardFront");
  const cardBack = document.getElementById("cardBack");
  const cardInner = document.getElementById("flashcardInner");
  const cardCount = document.getElementById("cardCount");

  fetch('/api/flashcards')
    .then(res => res.json())
    .then(data => {
      flashcards = data;
      showCard(currentIndex);
    });

  function showCard(index) {
    const [question, answer] = flashcards[index];
    cardFront.textContent = question;
    cardBack.textContent = answer;
    flashcard.classList.remove("flipped");
    cardCount.textContent = `Card ${index + 1} of ${flashcards.length}`;
  }

  function nextCard() {
    if (currentIndex < flashcards.length - 1) {
      currentIndex++;
      showCard(currentIndex);
    }
  }

  function prevCard() {
    if (currentIndex > 0) {
      currentIndex--;
      showCard(currentIndex);
    }
  }

  flashcard.addEventListener("click", () => {
    flashcard.classList.toggle("flipped");
  });

  function uploadPDF() {
    const fileInput = document.getElementById("pdfInput");
    const file = fileInput.files[0];
    if (!file) {
      alert("Please select a PDF file.");
      return;
    }

    const formData = new FormData();
    formData.append("file", file);

    document.getElementById("loadingSpinner").style.display = "flex";

    fetch("/upload_pdf", {
      method: "POST",
      body: formData,
    })
      .then((res) => res.json())
      .then((data) => {
        flashcards = data;
        currentIndex = 0;
        showCard(currentIndex);
        alert("PDF processed successfully!");
      })
      .catch((err) => {
        console.error(err);
        alert("Failed to upload PDF.");
      })
      .finally(() => {
        document.getElementById("loadingSpinner").style.display = "none";
      });
  }

  function sendText() {
    const text = document.getElementById("textInput").value;
    if (!text.trim()) {
      alert("Please enter some text.");
      return;
    }

    document.getElementById("loadingSpinner").style.display = "flex";

    fetch("/upload_text", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ text: text }),
    })
      .then((res) => res.json())
      .then((data) => {
        flashcards = data;
        currentIndex = 0;
        showCard(currentIndex);
        alert("Text processed successfully!");
      })
      .catch((err) => {
        console.error(err);
        alert("Failed to process text.");
      })
      .finally(() => {
        document.getElementById("loadingSpinner").style.display = "none";
      });
  }