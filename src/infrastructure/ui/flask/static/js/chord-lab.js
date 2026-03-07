  const NOTES = ['C','C#','D','D#','E','F','F#','G','G#','A','A#','B'];

  const defaults = [
    { note: 'C', octave: 4, tone: 'major' },
    { note: 'F', octave: 4, tone: 'major' },
    { note: 'G', octave: 4, tone: 'major' },
    { note: 'A', octave: 4, tone: 'minor' },
  ];

  function getChordName(s) {
    let name = s.note + (s.tone === 'minor' ? 'm' : '');
    if (s.maj7) name += 'maj7';
    else if (s.min7) name += '7';
    return name;
  }

  function createBlock(state) {
    const block = document.createElement('div');
    block.className = 'chord-block';
    block.innerHTML = `
      <p class="chord-name">${getChordName(state)}</p>

      <label>Note
        <select class="sel-note">
          ${NOTES.map(n => `<option ${n === state.note ? 'selected' : ''}>${n}</option>`).join('')}
        </select>
      </label>

      <label>Octave
        <select class="sel-octave">
          ${[1,2,3,4,5,6,7].map(o => `<option ${o === state.octave ? 'selected' : ''}>${o}</option>`).join('')}
        </select>
      </label>

      <label>Tone
        <select class="sel-tone">
          <option value="major" ${state.tone === 'major' ? 'selected' : ''}>Major</option>
          <option value="minor" ${state.tone === 'minor' ? 'selected' : ''}>Minor</option>
        </select>
      </label>

      <label><input type="checkbox" class="cb-maj7"> 7th Maior (maj7)</label>
      <label><input type="checkbox" class="cb-min7"> 7th Menor (7)</label>
    `;

    const name    = block.querySelector('.chord-name');
    const selNote = block.querySelector('.sel-note');
    const selOct  = block.querySelector('.sel-octave');
    const selTone = block.querySelector('.sel-tone');
    const cbMaj7  = block.querySelector('.cb-maj7');
    const cbMin7  = block.querySelector('.cb-min7');

    function update() { name.textContent = getChordName(state); }

    selNote.addEventListener('change', e => { state.note   = e.target.value;  update(); });
    selOct.addEventListener ('change', e => { state.octave = +e.target.value; update(); });
    selTone.addEventListener('change', e => { state.tone   = e.target.value;  update(); });

    cbMaj7.addEventListener('change', () => {
      state.maj7 = cbMaj7.checked;
      if (cbMaj7.checked) { state.min7 = false; cbMin7.checked = false; }
      update();
    });
    cbMin7.addEventListener('change', () => {
      state.min7 = cbMin7.checked;
      if (cbMin7.checked) { state.maj7 = false; cbMaj7.checked = false; }
      update();
    });

    return block;
  }

  const container = document.getElementById('chordsContainer');
  defaults.forEach(s => container.appendChild(createBlock(s)));