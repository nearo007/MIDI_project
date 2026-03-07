const NOTE_NAMES = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B'];
const IS_BLACK = [false, true, false, true, false, false, true, false, true, false, true, false];

const piano = document.getElementById('piano');
const MIDI_START = 21; // A0
const MIDI_END = 108; // C8
const WHITE_W = 32;
const BLACK_W = 20;

const keyData = [];
let whiteIndex = 0;

for (let midi = MIDI_START; midi <= MIDI_END; midi++) {
    const semitone = midi % 12;
    const octave = Math.floor(midi / 12) - 1;
    const name = NOTE_NAMES[semitone];
    const isBlack = IS_BLACK[semitone];
    keyData.push({ midi, semitone, octave, name, isBlack, whiteIndex: isBlack ? null : whiteIndex });
    if (!isBlack) whiteIndex++;
}

const container = document.createElement('div');
container.style.cssText = `position:relative; display:flex; height:160px; width:${whiteIndex * WHITE_W}px;`;

keyData.forEach(k => {
    if (!k.isBlack) {
        const div = document.createElement('div');
        div.className = 'key-white';
        div.innerHTML = `<form action="play" method="post">
            <input type="hidden" name="key_num" value="${k.midi}">
            <button type="submit">${k.name}${k.octave}</button>
          </form>`;
        container.appendChild(div);
    }
});

keyData.forEach(k => {
    if (k.isBlack) {
        const prev = keyData.find(x => x.midi === k.midi - 1);
        if (!prev) return;
        const left = prev.whiteIndex * WHITE_W + WHITE_W - BLACK_W / 2 - 2;

        const div = document.createElement('div');
        div.className = 'key-black';
        div.style.left = left + 'px';
        div.innerHTML = `<form action="play" method="post">
            <input type="hidden" name="key_num" value="${k.midi}">
            <button type="submit"></button>
          </form>`;
        container.appendChild(div);
    }
});

piano.appendChild(container);