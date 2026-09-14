Add-Type -AssemblyName System.Speech
$out = Join-Path $PSScriptRoot 'render-work'
New-Item -ItemType Directory -Path $out -Force | Out-Null
$scenes = Get-Content -Raw (Join-Path $PSScriptRoot 'cut-55s.json') | ConvertFrom-Json
$voice = New-Object System.Speech.Synthesis.SpeechSynthesizer
$voice.SelectVoice('Microsoft David Desktop')
$voice.Rate = 1
for ($i = 0; $i -lt $scenes.Count; $i++) {
  $voice.SetOutputToWaveFile((Join-Path $out ('voice-{0:D2}.wav' -f $i)))
  $spoken = $scenes[$i][3].Replace('Numens', 'Noo mens').Replace('Numen', 'Noo men')
  $voice.Speak($spoken)
  $voice.SetOutputToNull()
}
$voice.Dispose()
