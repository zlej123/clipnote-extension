const FIELDS = ["apiKey", "language", "model", "serverUrl"];
const DEFAULTS = { apiKey: "", language: "ko", model: "gemini-flash-lite-latest", serverUrl: "" };

chrome.storage.sync.get(FIELDS).then((saved) => {
  for (const field of FIELDS) {
    document.getElementById(field).value = saved[field] ?? DEFAULTS[field];
  }
});

document.getElementById("save").onclick = async () => {
  const values = {};
  for (const field of FIELDS) values[field] = document.getElementById(field).value.trim();
  if (!values.model) values.model = DEFAULTS.model;
  await chrome.storage.sync.set(values);
  document.getElementById("saved").style.display = "block";
  setTimeout(() => (document.getElementById("saved").style.display = "none"), 1500);
};
