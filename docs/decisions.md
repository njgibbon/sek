# Decisions

* One Check Set per Cloud Service. Not sub-checks. For example was going to have 'EKS' which would be 'Manage Service' and 'Nodes' where both could be run or either in isolation. But, decided to simplify and merge in to one.

* Not using 'Black' formatting. Don't like how some of it looks, it's not GA stable and I worry about all of the edge cases which are raised against the tool. I don't feel super strongly about this decision, but that's it for now. Using other tools which effect formatting.

* Design will focus on sanley minimising network requests. So, individual check independence will not be the highest ideal. For example all EKS checks there will only need to be a single `descirbe_cluster` request and this data will be passed to all checks that require the information. The check will not make the request again. Reuse and common interfaces will be very important and a core part of the design too.
