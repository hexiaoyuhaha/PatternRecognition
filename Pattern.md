# Pattern Recognition


<img src="images/regexp-date.png" width="400"/>
<img src="images/regexp-email.png" width="400"/>

<!--![Date Detection](images/regexp-date.png)
![Email Detection](images/regexp-email.png)-->




##	Pattern Recognition using open source libraries 
 

<img src="images/google-parser-phone.png" width="400"/>


#### "FirstName"
#### "LastName"
#### "Address1"
#### "Address2"
#### "City"
#### "State"

For matching state abbreviation

```
Ala|Ariz|[A]z|[A]rk|Calif|Colo|Conn|Ct|Dak|[D]el|Fla|Ga|[I]ll|Ind|Kans?|Ky|[L]a|[M]ass|Md|Mich|Minn|[M]iss|Mo|Mont|Neb|Nev|Okla|[O]re|[P]a|Penn|Tenn|[T]ex|Va|Vt|[W]ash|Wisc?|Wyo
```

#### "Zip"

```
^[0####9]{5}(?:####[0####9]{4})?$
```

#### "CellPhone" : 

```
^(?:(?:\+?1\s*(?:[.####]\s*)?)?(?:\(\s*([2####9]1[02####9]|[2####9][02####8]1|[2####9][02####8][02####9])\s*\)|([2####9]1[02####9]|[2####9][02####8]1|[2####9][02####8][02####9]))\s*(?:[.####]\s*)?)?([2####9]1[02####9]|[2####9][02####9]1|[2####9][02####9]{2})\s*(?:[.####]\s*)?([0####9]{4})(?:\s*(?:#|x\.?|ext\.?|extension)\s*(\d+))?$
```

#### "Phone"
is the format different than cell phone?

#### "DOB"

```
\d{1,2}[\####\/]\d{1,2}[\####\/]\d{2,4}
```
If contains alphabets

1. Contains (month name or short names such as September, Sept, Sep)

Else

1. Split by / or –
2. Check if splits are numeric of length 2,2, 4 or 2,2,2, or 1,1,2 or 1,1,4. 

For first 2 fields, range must be within 1####30 for one and 1####12 for other
    
#### "Gender"
Does not need anonymization
#### "Carrier"
Carriers can be assigned codes in obfuscation
#### "SiteName"
Not sure what this field is