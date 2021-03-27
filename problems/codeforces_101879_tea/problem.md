
https://codeforces.com/gym/101879/problem/I

Tea is second most consumed beverage in the world after water, especially in the United Kingdom, where about 84% of the population has tea every day. This British tradition with tea is a well known fact. What few people know is that English tea has its origins in Portugal. In 1662, when Catarina de Bragança married King Charles II of England, she traveled to London and took with her some tea leaves. The story goes that the boxes where these leaves were carried were labeled as "Transport of Aromatic Herbs", later abbreviated in Portuguese to TEA.

The historian Gaia "the Curious" Fontenelle is studying some old documents that describe how tea was transported from Portugal to England. Initially, N boats were anchored in Portugal. Each boat was assigned a distinct integer between 1 and N. The documents say that the tea was to be transported in a total of K trips. These trips would use ports in Portugal, China and England. After many ruminations, Gaia reached these conclusions:

1. In each one of the K trips only one boat would move between two ports. Moreover, this boat was the smallest numbered when considering the boats stationed in both ports.
2. The trips would take place one after the other, and there never were two boats traveling at the same time.
3. Boat N would end its itinerary when it arrived in England. For i<N, boat i would only end its itinerary when it arrived in England and the itinerary of boat i+1 had also ended.

Gaia quickly noticed that, with these rules, each port looks like a stack, where a trip corresponds to moving the smallest boat (in the top) of the origin stack to the destination stack (while satisfying constraint 1). Gaia was used to dealing with imprecise or downright false sources of information, so she started playing in her notebooks and she realized that, depending on the values of N and K, sometimes it was impossible to move all N boats (even while using the port in China). For this reason, for each report about tea transport, she wants to find out whether it was possible or not.

Gaia got hungry and left for coffee, chocolate and taking pictures of the sunset. You are an intern in her team and wish to impress her (maybe you will get the job this way). Thus, you decided to solve the problem before she returns.

### Input
The input has a single input line with integers N and K, the number of boats and the total number of trips by the boats, respectively.

### Constraints

    1≤N≤21
    1≤K≤2^21

### Output
In the first line print "Y" (without quotes) if it is possible to move the N boats from Portugal to England, while respecting the constraints described above. Otherwise, print "N". If the answer is affirmative, print K lines that describe a itinerary of trips that moves the N boats. To represent a trip from port X to port Y, print "X Y". Each port is represented by a character as follows:

- Portugal: "A"
- China: "B"
- England: "C"

If there is more than one possible itinerary, any one will be accepted.
