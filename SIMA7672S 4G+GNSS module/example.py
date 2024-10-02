from SIMA7672S import SIMA7672S
import time

sim = SIMA7672S()
URL = "http://www.testingmcafeesites.com/" #it can be https also

httpResponse = sim.HTTP.SendHTTPRequest(URL, sim.HTTP.HTTPRequest.GET, debug=True)
time.sleep(1)
if httpResponse and httpResponse[1] != 200:
    print(sim.HTTP.ReadHTTPResponse(httpResponse[2]))
elif httpResponse:
    print(sim.HTTP.ReadHTTPResponse(httpResponse[2]))
time.sleep(1)
sim.HTTP.terminateHTTP(debug=True)