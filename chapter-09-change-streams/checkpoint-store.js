const fs = require("fs");

const CHECKPOINT_FILE = "resume_token.json";

function saveResumeToken(token) {

  fs.writeFileSync(
    CHECKPOINT_FILE,
    JSON.stringify(token, null, 2)
  );

  console.log("Resume token saved");
}

function loadResumeToken() {

  if (!fs.existsSync(CHECKPOINT_FILE)) {
    return null;
  }

  const data = fs.readFileSync(
    CHECKPOINT_FILE,
    "utf-8"
  );

  console.log("Resume token loaded");

  return JSON.parse(data);
}

module.exports = {
  saveResumeToken,
  loadResumeToken
};