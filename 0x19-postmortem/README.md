<h1>Postmortem : E-commerce website experience outage</h1>

<h2>Issue Summary:</h2>

On March 1st, 2023, from 10:00 AM to 12:00 PM, our company's e-commerce website experienced an outage. The issue impacted all users attempting to access the website, with 100% of our user base being affected. Users experienced slow page load times, inability to access the website, and some reported error messages.

<h2>Root Cause:</h2>

The root cause of the issue was due to a misconfiguration of our web server's load balancer. One of our junior engineers mistakenly updated the load balancer's settings, causing it to route all incoming traffic to a single server instance, which eventually became overloaded and crashed, leading to the complete outage.

<h2>Timeline:</h2>

- 10:00 AM - Our monitoring system detected a significant increase in server errors and latency on our e-commerce website.

- 10:05 AM - Our on-call engineer received an alert and started investigating the issue.

- 10:15 AM - The engineer noticed that all incoming traffic was being routed to a single server instance, causing it to become overloaded and crash.

- 10:30 AM - The engineer attempted to restart the crashed server instance, but the issue persisted.

- 11:00 AM - The engineer escalated the issue to the senior engineering team and started investigating the web server's load balancer configuration.

- 11:30 AM - The senior engineering team identified the misconfigured load balancer and quickly rolled back the change, restoring normal website functionality.

<h2>Resolution:</h2>

To fix the issue, the senior engineering team rolled back the misconfigured load balancer settings to the previous working configuration. They also implemented an automatic roll-back mechanism that reverts any changes made to the load balancer if it detects any anomalies.

<h2>Corrective and Preventative Measures:</h2>

To prevent similar issues in the future, we will be implementing the following corrective and preventative measures:

- Provide additional training and documentation for junior engineers to ensure they understand our web stack configurations and best practices.

- Implement a more robust monitoring system to detect anomalies and potential issues before they affect our users.

- Set up a process to review and approve any changes made to our web stack by junior engineers before they are implemented.

- Regularly perform load testing to identify potential performance bottlenecks and ensure we have the necessary resources to handle peak traffic.

- Implement a disaster recovery plan to quickly recover from any future outages.

<h2>In summary</h2>
the outage on March 1st was caused by a misconfigured load balancer that routed all incoming traffic to a single server instance, leading to an overload and crash. The issue was resolved by rolling back the misconfigured settings and implementing an automatic roll-back mechanism. Going forward, we will be implementing several corrective and preventative measures to prevent similar issues and improve our overall web stack reliability. 

And to the junior engineer responsible for the misconfiguration: we forgive you for now, unless you do it again...
