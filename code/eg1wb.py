import thinkdsp

sin_sig = thinkdsp.SinSignal(freq=440,amp=1.0,offset=0)
cos_sig = thinkdsp.CosSignal(freq=330,amp=1.0,offset=0)
sum_sig = sin_sig + cos_sig
sin_sig.plot()
cos_sig.plot()
sum_sig.plot()
#plt.show()

wave_sin = sin_sig.make_wave()
wave_cos = cos_sig.make_wave()
wave_sum = sum_sig.make_wave()

plt.figure()
plt.ion()
sum_sig.plot()
sin_sig.plot()
cos_sig.plot()
plt.show()

want_to_play = input("Do you want to play from C to B? y/n?")
if want_to_play == 'y':

    freq = int(input("Enter the frequency you want to play(262 Hz for middle C): "))
    ratio = 2**(1/12)
    for i in range(12):
       if i not in [1,3,6,8,10]:
    
           sample_sig = thinkdsp.SinSignal(freq*ratio**(i))
           wave_sample = sample_sig.make_wave()
#sample_sig = thinkdsp.SinSignal(freq)
#wave_sample = sample_sig.make_wave()
           wave_sample.play()
           print("\n Playing: frequency is: ",freq*ratio**i," Hz")
    if i == 0:
        wave_C = wave_sample
