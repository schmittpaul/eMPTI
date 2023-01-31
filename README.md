# eMPTI experiment code

## Dependencies
We require browsertime. Install:

```
npm install browsertime
```

## Notes
- By default browsertime results will save in a `browsertime-results` directory. Be sure to move the results from a relay or non-relay run into their own respective directories once complete, e.g.:
    ```
    python browsertime_driver.py
    mv browsertime-results browsertime-results-no-relay
    
    ENABLE RELAY

    python browsertime_driver.py
    mv browsertime-results browsertime-results-relay
    ```

- tranco_list.txt is the top 1000 websites listed on the Tranco list as of January 27, 2023 